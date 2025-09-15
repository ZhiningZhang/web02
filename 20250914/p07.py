import pandas as pd
import pdfplumber
import re

pdf_path = r"C:\Hannah\20250914\Female 40 - Pacific Life IUL - 20M - 10pay@350K.pdf"

# 1) 从 PDF 重新提取“年度表”数据
rows = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text and "Policy Values: Tabular Detail" in text:
            lines = text.splitlines()
            for line in lines:
                # 匹配以“Year Age ...”格式开头的每一行
                if re.match(r"^\s*\d+\s+\d+", line):
                    parts = re.split(r"\s+", line.strip())
                    # 期望至少包含 年度 年龄 缴费 + 9 个数值 共 12 列
                    if len(parts) >= 12:
                        year, age, outlay = parts[0:3]
                        values = parts[3:12]
                        try:
                            row = [int(year), int(age), float(outlay.replace(",", ""))] + [
                                float(v.replace(",", "")) if v != "-" else 0 for v in values
                            ]
                            rows.append(row)
                        except:
                            pass

# 2) 组装为中文列名
columns_cn = [
    "年度", "年龄", "缴费",
    "保证累积价值", "保证退保价值", "保证身故赔偿",
    "非保证替代累积价值", "非保证替代退保价值", "非保证替代身故赔偿",
    "非保证当前累积价值", "非保证当前退保价值", "非保证当前身故赔偿"
]
df_cn = pd.DataFrame(rows, columns=columns_cn)

# 3) 构建“阅读指南”工作表
guide = pd.DataFrame({
    "字段": [
        "年度", "年龄", "缴费",
        "保证累积价值", "保证退保价值", "保证身故赔偿",
        "非保证替代累积价值", "非保证替代退保价值", "非保证替代身故赔偿",
        "非保证当前累积价值", "非保证当前退保价值", "非保证当前身故赔偿",
        "使用建议"
    ],
    "说明": [
        "保单第几年度，从 1 到 70+。",
        "对应被保险人的实际年龄，从 40 到 109。",
        "当年应缴保费。此计划演示为前 10 年每年 35 万美元，第 11 年起 0。",
        "在最保守假设下的保单累积价值。",
        "在最保守假设下的可退保拿到的现金价值。",
        "在最保守假设下的身故赔偿金额。",
        "较低增长假设下的保单累积价值。",
        "较低增长假设下的可退保现金价值。",
        "较低增长假设下的身故赔偿金额。",
        "当前演示利率假设下的保单累积价值。",
        "当前演示利率假设下的可退保现金价值。",
        "当前演示利率假设下的身故赔偿金额。",
        "常见查看方式：按年龄筛选；比较“保证”和“当前”两列的差异；用“非保证当前退保价值”估算可贷款额度。实际操作前请向保险公司索取在保试算。"
    ]
})

# 4) 导出为 Excel（中文解释版，多工作表）
xlsx_path = r"C:\Hannah\20250914\PacificLife_IUL_Projection.csvPacificLife_IUL_完整年度_中文解释.xlsx"
with pd.ExcelWriter(xlsx_path) as writer:
    df_cn.to_excel(writer, sheet_name="年度明细", index=False)
    guide.to_excel(writer, sheet_name="阅读指南", index=False)

xlsx_path
