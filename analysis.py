"""Does uploading more videos earn a YouTube channel more?

Usage: python analysis.py path/to/Global_YouTube_Statistics.csv
The dataset is the sample file shipped with Avaloka:
https://github.com/guruvaidev/avaloka/blob/main/app/sample_data/Global_YouTube_Statistics.csv
"""
import sys
import pandas as pd

path = sys.argv[1]
df = pd.read_csv(path, encoding="latin1").rename(columns={"video views": "views"})

# ---- data quality ----
dq = {
    "rows": len(df),
    "zero_view_channels": int((df.views == 0).sum()),
    "zero_view_but_over_1M_subs": int(((df.views == 0) & (df.subscribers > 1e6)).sum()),
    "missing_category": int(df.category.isna().sum()),
    "missing_country": int(df.Country.isna().sum()),
    "zero_uploads": int((df.uploads == 0).sum()),
    "zero_earnings": int((df.highest_yearly_earnings == 0).sum()),
}
print("DATA QUALITY"); [print(f"  {k}: {v}") for k, v in dq.items()]

# ---- earnings per 1,000 views ----
g = df[df.views > 0].copy()
g["earn_per_1k_views"] = g.highest_yearly_earnings / g.views * 1000
cat = (g.groupby("category").earn_per_1k_views.agg(n="size", median="median", mean="mean")
         .query("n >= 10").sort_values("median", ascending=False).round(3))
ctry = (g.groupby("Country").earn_per_1k_views.agg(n="size", median="median")
          .query("n >= 15").sort_values("median", ascending=False).round(3))
print("\nBY CATEGORY (median $ per 1k views, n>=10)\n", cat)
print("\nBY COUNTRY (median $ per 1k views, n>=15)\n", ctry)
cat.to_csv("earnings_per_1k_by_category.csv"); ctry.to_csv("earnings_per_1k_by_country.csv")

# ---- uploads vs channel age ----
d = df[(df.views > 0) & (df.uploads > 0) & (df.created_year >= 2005)].copy()
d["age"] = 2026 - d.created_year
d["earn_per_1k_views"] = d.highest_yearly_earnings / d.views * 1000
print("\nSPEARMAN CORRELATIONS")
for t in ["subscribers", "highest_yearly_earnings", "earn_per_1k_views"]:
    print(f"  {t}: uploads={d.uploads.corr(d[t], method='spearman'):.3f}  "
          f"age={d.age.corr(d[t], method='spearman'):.3f}")
d["upload_quartile"] = pd.qcut(d.uploads, 4, labels=["Q1 fewest", "Q2", "Q3", "Q4 most"])
q = d.groupby("upload_quartile", observed=True).agg(
    n=("uploads", "size"), max_uploads=("uploads", "max"),
    median_subs=("subscribers", "median"),
    median_yearly_earnings=("highest_yearly_earnings", "median"),
    median_earn_per_1k=("earn_per_1k_views", "median")).round(2)
print("\nBY UPLOAD QUARTILE\n", q)
q.to_csv("by_upload_quartile.csv")
