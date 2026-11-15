# Avaloka mission `0cb577ad66f9`

**Goal:** average uploads by category

This bundle was produced by Avaloka as a governed *Data Mission* — an outcome, not an interaction. Economic multiplier: **11.1x** (≈15.2 manual hours compressed).

## Deliverables

- `executive_report.html` — the decision-maker summary
- `technical_report.html` — full methodology, schema, quality and validation
- `analysis.ipynb` / `analysis.py` — reproducible pipeline
- `transformed_dataset.parquet` — cleaned working dataset
- `data_quality.json`, `validation_report.json`, `planner_graph.json` — evidence
- `assumptions.yaml`, `lineage.json`, `environment.lock` — governance & reproducibility
- `goal_analysis.json` — measured answer to the stated goal

## Key findings

- category=News & Politics: mean uploads=1.12e+05.
- category=Nonprofits & Activism: mean uploads=1.03e+05.
- category=Shows: mean uploads=2.74e+04.
- category=Sports: mean uploads=1.45e+04.
- category=Entertainment: mean uploads=1.19e+04.

## Limitations

- High-missingness columns require an explicit imputation policy.
- Estimated manual effort and value are heuristics pending customer calibration.

## Reproduce

```bash
avaloka analyze app/sample_data/Global_YouTube_Statistics.csv --goal 'average uploads by category' --output ./reproduced-analysis
```

---
_Reproduce or adapt this mission with `avaloka`._