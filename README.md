# Does uploading more earn a YouTube channel more?

An analysis of 995 of the world's top YouTube channels, built for the Avaloka
engineering-intern hackathon. Avaloka (https://avaloka.ai) profiled the dataset and
flagged its quality problems; the earnings analysis itself was computed in code
(`analysis.py`) and checked against the raw CSV.

**Question:** Does uploading more videos earn a channel more? How do earnings per 1,000
views differ by category and country? Do uploads or channel age explain subscribers and
earnings better? What data-quality problems distort the answer?

**Dataset:** `Global_YouTube_Statistics.csv`, the sample shipped with Avaloka
(995 rows, 28 columns). Earnings columns are estimates, not reported revenue.

## Answer in one paragraph

More uploads raise a channel's **total** earnings (Spearman 0.39), but not its
subscribers (0.05), and earnings **per 1,000 views** rise only up to the middle of the
pack and then flatten. What a view is worth depends far more on **category and audience
country** than on posting volume. Channel age barely matters for earnings (-0.03).

## Findings

**Median highest-yearly-earnings per 1,000 views, by category** (channels with views > 0, n >= 10)

| Category | n | Median $ |
|---|---|---|
| Science & Technology | 17 | 0.69 |
| News & Politics | 26 | 0.68 |
| Shows | 13 | 0.61 |
| Sports | 11 | 0.51 |
| Education | 45 | 0.44 |
| People & Blogs | 132 | 0.42 |
| Comedy | 69 | 0.41 |
| Film & Animation | 45 | 0.40 |
| Music | 202 | 0.35 |
| Entertainment | 241 | 0.33 |
| Howto & Style | 40 | 0.30 |
| Gaming | 94 | 0.29 |

**By country** (n >= 15): India 0.67, Russia 0.50, Brazil 0.48, Indonesia 0.43,
Mexico 0.35, South Korea 0.34, United States 0.33, United Kingdom 0.31, Thailand 0.26,
Canada 0.17, Spain 0.15. Full tables in `earnings_per_1k_by_*.csv`.

**Uploads vs channel age (Spearman, 2005+ channels with views and uploads > 0)**

| Outcome | Uploads | Channel age |
|---|---|---|
| Subscribers | 0.05 | 0.10 |
| Highest yearly earnings | 0.39 | -0.03 |
| Earnings per 1,000 views | 0.30 | n/a |

**By upload quartile** (`by_upload_quartile.csv`)

| Uploads | Max uploads | Median yearly earnings | Median $ per 1k views |
|---|---|---|---|
| Q1 fewest | 240 | 0.73M | 0.17 |
| Q2 | 796 | 2.75M | 0.42 |
| Q3 | 2,905 | 3.50M | 0.52 |
| Q4 most | 301,308 | 5.10M | 0.47 |

Reading: volume helps up to roughly the Q3 range, then yield per view stops improving.
This is correlation, not causation: bigger channels both upload more and earn more.

## Data-quality problems that distort the answer

- **8 channels report 0 video views but over 1 million subscribers.** Impossible; the views field is broken for them, so they are excluded from per-view figures.
- **46 rows have no category and 122 have no country.** Category and country charts silently drop them (Avaloka's own chart notes say "Rows with no category are left out").
- **43 channels show 0 uploads and 79 show 0 earnings**, which would skew averages if kept.
- **Extreme outliers.** The top views bin holds 12 channels above 57 billion views, and the earnings histogram's top bin holds 11 channels above $74M. Medians are used instead of means for this reason.
- **Earnings are estimates**, so the per-1,000-view dollars are indicative, not audited revenue.

## What Avaloka did and did not do

- Auto Insights profiled the file (995 rows, 28 columns, domain "Media/YouTube Analytics"),
  reported empty cells (e.g. 33.9% of `subscribers_for_last_30_days`, 12.3% of country-linked columns,
  4.6% of `category`) and built four charts.
- Its Insights Assistant is limited to those charts, so it could not compute earnings per 1,000 views
  or the correlations. It did correctly flag zero-view channels, rows dropped for missing category
  or country, and extreme outliers.
- The open-source Avaloka CLI (`avaloka analyze`) also runs on this file offline and passes
  validation, but without an LLM key it returns a generic summary rather than answering a custom question.

## Reproduce

```bash
python analysis.py Global_YouTube_Statistics.csv
```

Needs Python 3 and pandas. Output is in `results.txt` and the CSV files.
