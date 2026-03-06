# ============================================================
# SciPy – Scientific Computing
# ============================================================
import numpy as np
from scipy import integrate, interpolate, optimize, signal, stats

print("=" * 50)
print("1. Statistics")
print("=" * 50)

rng = np.random.default_rng(seed=42)
data = rng.normal(loc=5.0, scale=2.0, size=200)

mean, std = data.mean(), data.std(ddof=1)
print(f"Sample mean: {mean:.4f}, std: {std:.4f}")

# t-test: is the mean significantly different from 5?
t_stat, p_val = stats.ttest_1samp(data, popmean=5.0)
print(f"One-sample t-test  t={t_stat:.4f}, p={p_val:.4f}")

# Pearson correlation
x_corr = rng.standard_normal(100)
y_corr = 3 * x_corr + rng.standard_normal(100)
r, p = stats.pearsonr(x_corr, y_corr)
print(f"Pearson r={r:.4f}, p={p:.4e}")

print("\n" + "=" * 50)
print("2. Numerical Integration")
print("=" * 50)

# Definite integral of sin(x) from 0 to pi  (expected: 2.0)
result, error = integrate.quad(np.sin, 0, np.pi)
print(f"∫₀^π sin(x) dx = {result:.6f}  (error: {error:.2e})")

# 2-D integral of exp(-x^2 - y^2) (expected ≈ pi)
f2d = lambda y, x: np.exp(-x**2 - y**2)
result2, _ = integrate.dblquad(f2d, -5, 5, -5, 5)
print(f"∬ exp(-x²-y²) dx dy ≈ {result2:.6f}  (expected ≈ {np.pi:.6f})")

print("\n" + "=" * 50)
print("3. Optimization")
print("=" * 50)

# Find the minimum of f(x) = (x-3)^2 + 2
def f(x):
    return (x - 3) ** 2 + 2

result_opt = optimize.minimize_scalar(f, bounds=(0, 10), method="bounded")
print(f"Minimum of (x-3)²+2:  x={result_opt.x:.6f}, f(x)={result_opt.fun:.6f}")

# Root-finding: x^3 - x - 2 = 0  (root ≈ 1.5214)
root = optimize.brentq(lambda x: x**3 - x - 2, 1, 2)
print(f"Root of x³-x-2=0:  x={root:.6f}")

print("\n" + "=" * 50)
print("4. Interpolation")
print("=" * 50)

x_pts = np.array([0, 1, 2, 3, 4, 5], dtype=float)
y_pts = np.sin(x_pts)

cubic = interpolate.CubicSpline(x_pts, y_pts)
x_fine = np.linspace(0, 5, 50)
y_fine = cubic(x_fine)
print(f"Cubic spline at x=2.5: {cubic(2.5):.6f}  (sin(2.5)={np.sin(2.5):.6f})")

print("\n" + "=" * 50)
print("5. Signal Processing")
print("=" * 50)

# Low-pass Butterworth filter
fs = 1000.0          # sampling rate (Hz)
cutoff = 50.0        # cutoff frequency (Hz)
b, a = signal.butter(N=4, Wn=cutoff / (fs / 2), btype="low")
t = np.linspace(0, 1, int(fs), endpoint=False)
noisy_signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)
filtered = signal.filtfilt(b, a, noisy_signal)
print(f"Signal RMS before filter: {np.sqrt(np.mean(noisy_signal**2)):.4f}")
print(f"Signal RMS after  filter: {np.sqrt(np.mean(filtered**2)):.4f}")
