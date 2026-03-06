# ============================================================
# Matplotlib – Plotting
# ============================================================
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")  # non-interactive backend (safe in all environments)

x = np.linspace(0, 2 * np.pi, 300)

# -------------------------------------------------------
# 1. Line plot
# -------------------------------------------------------
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)", linestyle="--")
ax.set_title("Sine and Cosine")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
fig.tight_layout()
fig.savefig("line_plot.png", dpi=100)
print("Saved: line_plot.png")

# -------------------------------------------------------
# 2. Scatter plot
# -------------------------------------------------------
rng = np.random.default_rng(seed=42)
x_s = rng.standard_normal(200)
y_s = 2 * x_s + rng.standard_normal(200)

fig, ax = plt.subplots()
ax.scatter(x_s, y_s, alpha=0.5, s=20)
ax.set_title("Scatter Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
fig.savefig("scatter_plot.png", dpi=100)
print("Saved: scatter_plot.png")

# -------------------------------------------------------
# 3. Bar chart
# -------------------------------------------------------
cities = ["Tehran", "Isfahan", "Shiraz", "Tabriz"]
populations = [9.3, 2.2, 1.9, 1.7]

fig, ax = plt.subplots()
ax.bar(cities, populations, color="steelblue")
ax.set_title("City Populations (millions)")
ax.set_ylabel("Population (M)")
fig.tight_layout()
fig.savefig("bar_chart.png", dpi=100)
print("Saved: bar_chart.png")

# -------------------------------------------------------
# 4. Histogram
# -------------------------------------------------------
data = rng.normal(loc=50, scale=10, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor="black", color="salmon")
ax.set_title("Histogram of Normal Distribution")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
fig.tight_layout()
fig.savefig("histogram.png", dpi=100)
print("Saved: histogram.png")

# -------------------------------------------------------
# 5. Subplots (2x2 grid)
# -------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x), color="orange")
axes[0, 1].set_title("cos(x)")

axes[1, 0].plot(x, np.tan(np.clip(x, -1.5, 1.5)), color="green")
axes[1, 0].set_title("tan(x) (clipped)")

axes[1, 1].plot(x, np.exp(-x / (2 * np.pi)) * np.sin(x), color="red")
axes[1, 1].set_title("Damped sine")

for ax in axes.flat:
    ax.grid(True)

fig.tight_layout()
fig.savefig("subplots.png", dpi=100)
print("Saved: subplots.png")
