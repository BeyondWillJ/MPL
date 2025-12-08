#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
from datetime import datetime

# 计算从开始日期到结束日期的天数。日期格式：YYYY-MM-DD。缺省值使用当前日期。

def parse_date(s, label):
    if s is None:
        return datetime.today().date()
    s = s.strip()
    if not s:
        print(f"{label} 为空，期望格式 YYYY-MM-DD。")
        sys.exit()
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        print(f"{label} 格式错误，期望 YYYY-MM-DD（例如 2025-12-08）。")
        sys.exit()


parser = argparse.ArgumentParser(description="计算从开始日期到结束日期的天数。日期格式：YYYY-MM-DD。缺省值使用当前日期。")
parser.add_argument("-s", "--start", help="开始日期，格式：YYYY-MM-DD（缺省为今天）", default=None)
parser.add_argument("-e", "--end", help="结束日期，格式：YYYY-MM-DD（缺省为今天）", default=None)

args = parser.parse_args()

start_str = args.start
end_str = args.end

start = parse_date(start_str, "开始日期")
end = parse_date(end_str, "结束日期")

print(f"相差 {(end - start).days} 天")

