# ============================================================
# Pandas – Data Analysis
# ============================================================
import numpy as np
import pandas as pd

# --- Build a synthetic dataset ---
rng = np.random.default_rng(seed=0)
n = 100

df = pd.DataFrame({
    "day":         pd.date_range("2024-01-01", periods=n, freq="D"),
    "temperature": rng.normal(loc=20.0, scale=5.0, size=n).round(1),
    "humidity":    rng.uniform(30, 90, size=n).round(1),
    "city":        rng.choice(["Tehran", "Isfahan", "Shiraz"], size=n),
})

# Inject a few missing values
df.loc[rng.choice(n, 5, replace=False), "temperature"] = np.nan

print("First 5 rows:\n", df.head())
print("\nInfo:")
df.info()

# --- Missing value handling ---
print("\nMissing values:\n", df.isnull().sum())
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
print("After fill – missing values:\n", df.isnull().sum())

# --- Descriptive statistics ---
print("\nDescriptive stats:\n", df[["temperature", "humidity"]].describe())

# --- Resample: monthly mean temperature ---
df_indexed = df.set_index("day")
monthly = df_indexed["temperature"].resample("ME").mean().round(2)
print("\nMonthly mean temperature:\n", monthly)

# --- Groupby city ---
city_stats = df.groupby("city")[["temperature", "humidity"]].agg(["mean", "std"]).round(2)
print("\nCity statistics:\n", city_stats)

# --- Correlation ---
corr = df[["temperature", "humidity"]].corr()
print("\nCorrelation matrix:\n", corr)

# --- Top 5 hottest days ---
hottest = df.nlargest(5, "temperature")[["day", "city", "temperature"]]
print("\nTop 5 hottest days:\n", hottest.to_string(index=False))
