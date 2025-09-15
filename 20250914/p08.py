from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 注册中文字体 (Register Chinese font)
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

# Output PDF path
pdf_path = r"C:\Hannah\20250914\PacificLife_IUL_Projection_Explanation.pdf"

# Create PDF doc
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("Pacific Life – Horizon IUL 2 保单说明书 (Illustration Explanation)", styles['Title']))
story.append(Spacer(1, 12))

# Sections with bilingual explanation
sections = [
    ("保单基本信息 (Policy Basics)",
     "被保险人 (Insured): Female, Age 40<br/>"
     "健康等级 (Underwriting Class): Preferred Non-Tobacco<br/>"
     "保险金额 (Face Amount / Death Benefit): $20,000,000<br/>"
     "缴费方式 (Premium Payment): $350,000 annually for 10 years, then $0<br/>"
     "身故赔偿选项 (Death Benefit Option): A (Level Death Benefit)<br/>"
     "设计选项 (Design Option): Long-Term Performance"),

    ("保单功能 (Key Features)",
     "身故保障 (Death Benefit Protection): $20M death benefit.<br/>"
     "保费灵活性 (Flexible Premiums): Premiums adjustable after year 10.<br/>"
     "不失效保证 (No-Lapse Guarantee): Policy guaranteed until age 90.<br/>"
     "账户类型 (Account Types): Fixed (1% min, 4.5% current), Indexed tied to S&P500, Nasdaq QQQ, BlackRock Endura.<br/>"
     "演示利率 (Illustrated Rate): 6.33% on S&P500 account."),

    ("附加条款 (Riders)",
     "Enhanced Performance Factor Rider (EPFR): Classic, no cost.<br/>"
     "Age 90 No-Lapse Guarantee Rider: 保证至90岁不失效.<br/>"
     "Living Benefits Rider: 提前领取 in case of terminal/chronic illness.<br/>"
     "Interest Guarantee on Termination Rider: Minimum alternate value.<br/>"
     "Conversion Rider: 可转换到其他保单 at year 8."),

    ("投资与增长 (Cash Value Growth & Indexed Accounts)",
     "1-Year S&P500 (Cap 10%, Par 100%)<br/>"
     "1-Year QQQ (Cap 10.5%)<br/>"
     "BlackRock Endura Volatility Control<br/>"
     "2-Year Indexed Account (Cap 24%)<br/>"
     "5-Year High Participation (Par 110%)<br/>"
     "Floor protection: 0% or 1%<br/>"
     "Caps and Participation Rates limit returns."),

    ("税务 (Tax Information)",
     "符合 IRC 7702 (CVAT)<br/>"
     "Death Benefit: Tax-free under IRC 101(a)(1)<br/>"
     "Policy Loans/Withdrawals: May be tax-free, but MEC (Modified Endowment Contract) rules apply.<br/>"
     "7-Pay Test: Prevents overfunding leading to MEC.")
]

# Add sections to story
for title, content in sections:
    story.append(Paragraph(title, styles['Heading2']))
    story.append(Paragraph(content, styles['Normal']))
    story.append(Spacer(1, 12))

# Sample table with illustration values
data = [
    ["Year", "Age", "Premium", "Guaranteed Cash Value", "Guaranteed DB", "Current Cash Value", "Current DB"],
    [1, 40, "$350,000", "$159,594", "$20,000,000", "$246,420", "$20,000,000"],
    [5, 44, "$350,000", "$790,270", "$20,000,000", "$1,391,560", "$20,000,000"],
    [10, 49, "$350,000", "$1,957,743", "$20,000,000", "$3,401,046", "$20,000,000"],
    [20, 59, "$0", "$0", "$20,000,000", "$7,087,371", "$20,000,000"],
    [40, 79, "$0", "$0", "$20,000,000", "$22,000,000+", "$20,000,000"],
    [60, 99, "$0", "$0", "$0", "$30,775,514", "$80,930,048"],
    [65, 104, "$0", "$0", "$0", "$38,331,599", "$108,199,000+"]
]

table = Table(data, repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("FONTSIZE", (0,0), (-1,-1), 8)
]))
story.append(Paragraph("演示现金价值与身故赔偿 (Illustrated Values)", styles['Heading2']))
story.append(table)

# Build PDF
doc.build(story)
pdf_path
