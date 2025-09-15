import matplotlib.pyplot as plt
import pandas as pd

# 模拟保单现金价值在20年内的增长（Current vs Alternate）
years = list(range(1, 21))

# 假设：Current Scale 年化收益率 6%，Alternate Scale 年化收益率 4%
initial_value = 100000  # 初始现金价值
current_values = [initial_value * ((1 + 0.06) ** yr) for yr in years]
alternate_values = [initial_value * ((1 + 0.04) ** yr) for yr in years]

# 转为 DataFrame
df = pd.DataFrame({
    "Year": years,
    "Current Scale (6%)": current_values,
    "Alternate Scale (4%)": alternate_values
})

# 绘图
plt.figure(figsize=(10,6))
plt.plot(df["Year"], df["Current Scale (6%)"], label="Non-Guaranteed Current Scale (6%)", marker="o")
plt.plot(df["Year"], df["Alternate Scale (4%)"], label="Non-Guaranteed Alternate Scale (4%)", marker="s")

plt.title("Cash Value Growth Projection: Current vs. Alternate Scale", fontsize=14, fontweight="bold")
plt.xlabel("Policy Year")
plt.ylabel("Cash Value ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
