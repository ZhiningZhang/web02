import matplotlib.pyplot as plt
import numpy as np

# 指数回报范围
index_returns = np.linspace(-0.2, 0.2, 100)  # -20% to +20%

# 参数
floor = 0
cap = 0.12
participation_rates = [0.8, 1.0, 1.2]

plt.figure(figsize=(8,6))

for pr in participation_rates:
    credited_rate = index_returns * pr
    credited_rate = np.clip(credited_rate, floor, cap)
    plt.plot(index_returns*100, credited_rate*100, label=f"Participation {int(pr*100)}%")

plt.axhline(y=0, color="black", linestyle="--", linewidth=0.8)
plt.axvline(x=0, color="black", linestyle="--", linewidth=0.8)

plt.title("Participation Rate vs. Index Return", fontsize=14)
plt.xlabel("Index Return (%)")
plt.ylabel("Credited Rate to Policy (%)")
plt.legend()
plt.grid(True)
plt.show()
