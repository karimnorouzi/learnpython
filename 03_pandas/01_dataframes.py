# ============================================================
# Pandas – DataFrames
# ============================================================
import pandas as pd

# --- Creating a DataFrame from a dict ---
data = {
    "name":   ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "age":    [24, 30, 22, 35, 28],
    "score":  [88.5, 76.0, 92.3, 65.7, 81.0],
    "passed": [True, True, True, False, True],
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nShape:", df.shape)
print("Column dtypes:\n", df.dtypes)

# --- Basic selection ---
print("\nName column:\n", df["name"])
print("\nFirst 3 rows:\n", df.head(3))

# --- Filtering rows ---
top_scorers = df[df["score"] >= 80]
print("\nTop scorers (score >= 80):\n", top_scorers)

# --- Adding a new column ---
df["grade"] = df["score"].apply(
    lambda s: "A" if s >= 90 else ("B" if s >= 80 else "C")
)
print("\nWith grade column:\n", df)

# --- Sorting ---
sorted_df = df.sort_values("score", ascending=False)
print("\nSorted by score (desc):\n", sorted_df)

# --- Basic statistics ---
print("\nDescriptive stats:\n", df[["age", "score"]].describe())

# --- Grouping ---
passed_stats = df.groupby("passed")["score"].mean()
print("\nMean score by passed:\n", passed_stats)

# --- Reading / writing CSV (in-memory demo) ---
csv_text = df.to_csv(index=False)
print("\nCSV preview (first 200 chars):\n", csv_text[:200])
