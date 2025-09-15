import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Configure Matplotlib for Chinese characters ---
# You might need to change 'SimHei' to a font installed on your system.
plt.rcParams['font.sans-serif'] = ['SimHei']
# This line is to ensure the minus sign displays correctly.
plt.rcParams['axes.unicode_minus'] = False


# --- Data for Chart 1: Cash Surrender Value ---
csv_data = {
    'Age': [40, 49, 59, 70, 80, 90],
    'Guaranteed (0.00%)': [0, 1647510, 0, 0, 0, 0],
    'Intermediate (4.50%)': [0, 3458328, 5402527, 8921584, 13575875, 20599169],
    'Illustrated (6.33%)': [0, 3814403, 7087371, 14291119, 26733143, 47925570]
}
df_csv = pd.DataFrame(csv_data)

# --- Data for Chart 2: Death Benefit ---
db_data = {
    'Age': [40, 70, 71, 80, 90, 91],
    'Guaranteed': [20000000, 20000000, 20000000, 20000000, 20000000, 0],
    'Illustrated': [20000000, 20000000, 20721300, 32347103, 52718127, 55257380]
}
df_db = pd.DataFrame(db_data)


# --- Function to format Y-axis labels as millions of dollars in Chinese ---
def millions_formatter_chinese(x, pos):
    """Formats a number into a string representing millions in Chinese."""
    return f'${x/1_000_000:.0f}百万'

# --- Generate Chart 1: Cash Surrender Value Growth (in Chinese) ---
fig1, ax1 = plt.subplots(figsize=(12, 7))

ax1.plot(df_csv['Age'], df_csv['Guaranteed (0.00%)'], marker='o', linestyle='-', label='保证 (0.00%)')
ax1.plot(df_csv['Age'], df_csv['Intermediate (4.50%)'], marker='o', linestyle='-', label='中间 (4.50%)')
ax1.plot(df_csv['Age'], df_csv['Illustrated (6.33%)'], marker='o', linestyle='-', label='演示 (6.33%)')
ax1.axvline(x=49, color='red', linestyle='--', linewidth=1, label='保费停止缴付 (49岁)')

# Formatting the chart with Chinese labels
ax1.set_title('预计现金退保价值增长 💰', fontsize=16)
ax1.set_xlabel("受保人年龄", fontsize=12)
ax1.set_ylabel("现金退保价值 ($)", fontsize=12)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter_chinese))
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.legend()
plt.tight_layout()


# --- Generate Chart 2: Death Benefit Growth (in Chinese) ---
fig2, ax2 = plt.subplots(figsize=(12, 7))

ax2.plot(df_db['Age'], df_db['Guaranteed'], marker='o', linestyle='-', label='保证')
ax2.plot(df_db['Age'], df_db['Illustrated'], marker='o', linestyle='-', label='演示')

# Formatting the chart with Chinese labels
ax2.set_title('预计身故赔偿增长 📈', fontsize=16)
ax2.set_xlabel("受保人年龄", fontsize=12)
ax2.set_ylabel("身故赔偿 ($)", fontsize=12)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter_chinese))
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.legend()
plt.tight_layout()

# --- Show all generated charts ---
plt.show()