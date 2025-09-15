import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Data for Chart 1: Cash Surrender Value ---
# Data sourced from the tables on pages 20-23 of the provided PDF.
csv_data = {
    'Age': [40, 49, 59, 70, 80, 90],
    'Guaranteed (0.00%)': [0, 1647510, 0, 0, 0, 0],
    'Intermediate (4.50%)': [0, 3458328, 5402527, 8921584, 13575875, 20599169],
    'Illustrated (6.33%)': [0, 3814403, 7087371, 14291119, 26733143, 47925570]
}
df_csv = pd.DataFrame(csv_data)

# --- Data for Chart 2: Death Benefit ---
# Data sourced from the tables on pages 20-23 of the provided PDF.
db_data = {
    'Age': [40, 70, 71, 80, 90, 91],
    'Guaranteed': [20000000, 20000000, 20000000, 20000000, 20000000, 0],
    'Illustrated': [20000000, 20000000, 20721300, 32347103, 52718127, 55257380]
}
df_db = pd.DataFrame(db_data)


# --- Function to format Y-axis labels as millions of dollars ---
def millions_formatter(x, pos):
    """Formats a number into a string representing millions, e.g., $10M."""
    return f'${x/1_000_000:.0f}M'

# --- Generate Chart 1: Cash Surrender Value Growth ---
fig1, ax1 = plt.subplots(figsize=(12, 7))

ax1.plot(df_csv['Age'], df_csv['Guaranteed (0.00%)'], marker='o', linestyle='-', label='Guaranteed (0.00%)')
ax1.plot(df_csv['Age'], df_csv['Intermediate (4.50%)'], marker='o', linestyle='-', label='Intermediate (4.50%)')
ax1.plot(df_csv['Age'], df_csv['Illustrated (6.33%)'], marker='o', linestyle='-', label='Illustrated (6.33%)')

# Add a vertical line for when premium payments stop
ax1.axvline(x=49, color='red', linestyle='--', linewidth=1, label='Premium Payments Stop (Age 49)')

# Formatting the chart
ax1.set_title('Projected Cash Surrender Value Growth 💰', fontsize=16)
ax1.set_xlabel("Insured's Age", fontsize=12)
ax1.set_ylabel("Cash Surrender Value ($)", fontsize=12)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.legend()
plt.tight_layout()
plt.show()


# --- Generate Chart 2: Death Benefit Growth ---
fig2, ax2 = plt.subplots(figsize=(12, 7))

ax2.plot(df_db['Age'], df_db['Guaranteed'], marker='o', linestyle='-', label='Guaranteed')
ax2.plot(df_db['Age'], df_db['Illustrated'], marker='o', linestyle='-', label='Illustrated')

# Formatting the chart
ax2.set_title('Projected Death Benefit Growth 📈', fontsize=16)
ax2.set_xlabel("Insured's Age", fontsize=12)
ax2.set_ylabel("Death Benefit ($)", fontsize=12)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.legend()
plt.tight_layout()
plt.show()

