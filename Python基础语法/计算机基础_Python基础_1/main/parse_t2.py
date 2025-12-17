import re, json, sys, os

src = r"e:\BookTEST\MPC\Python基础语法\计算机基础_Python基础_1\t2"

text = open(src, encoding="utf-8").read()

# 先去掉 JS 风格注释（仅删除行首的 // 和多行 /* */，避免删除字符串内的 //）
text = re.sub(r'(?m)^[ \t]*//.*\n', '\n', text)
text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)

# 1) 给未加引号的键加上引号（简单正则，假设文件内键没有引号）
text = re.sub(r'([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', text)

# ...existing code...
def val_repl(m):
    v = m.group(1)
    if v in ("true", "false", "null"):
        return ": " + v + m.group(2)
    # 使用 json.dumps 来正确转义字符串
    return ": " + json.dumps(v, ensure_ascii=False) + m.group(2)

text = re.sub(r':\s*([A-Za-z_\$][A-Za-z0-9_\$]*)\s*([,\}])', val_repl, text)

def nested_repl(m):
    v = m.group(2)
    if v in ("true", "false", "null"):
        return m.group(1) + v + m.group(3)
    return m.group(1) + json.dumps(v, ensure_ascii=False) + m.group(3)
# 处理数组或嵌套位置里的裸标识符（例如 [dQ] / show_urls: [dQ]）
text = re.sub(r'([:\[\{,]\s*)([A-Za-z_\$][A-Za-z0-9_\$]*)(\s*[,}\]])', nested_repl, text)
# ...existing code...

# 额外处理数组或嵌套位置里的裸标识符（例如 [dQ] / show_urls: [dQ]）
def nested_repl(m):
    v = m.group(2)
    if v in ("true", "false", "null"):
        return m.group(1) + v + m.group(3)
    return m.group(1) + 'null' + m.group(3)

text = re.sub(r'([:\[\{,]\s*)([A-Za-z_\$][A-Za-z0-9_\$]*)(\s*[,}\]])', nested_repl, text)
# ...existing code...

# 3) 删除逗号后紧接 ] 或 } 的尾逗号
text = re.sub(r',\s*([\]\}])', r'\1', text)

# 4) 尝试解析并输出漂亮的 JSON，若成功写入 t2.json
out_path = src + ".json"  # e:\...\t2.json
try:
    obj = json.loads(text)
    json_text = json.dumps(obj, ensure_ascii=False, indent=2)
    print(json_text)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json_text)
    print("已把解析后的 JSON 写入:", out_path, file=sys.stderr)
except Exception as e:
    print("解析失败：", e, file=sys.stderr)
    if isinstance(e, json.JSONDecodeError):
        print(f"JSON 解析错误：{e.msg} 行{e.lineno} 列{e.colno}", file=sys.stderr)
    open(src + ".clean.json", "w", encoding="utf-8").write(text)
    print("已把清洗后的内容写到:", src + ".clean.json", file=sys.stderr)