# Avaloka mission `09ecb72f10e2`

**Goal:** average highest_yearly_earnings by category

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

- category=Shows: mean highest_yearly_earnings=2.44e+07.
- category=Autos & Vehicles: mean highest_yearly_earnings=1.32e+07.
- category=nan: mean highest_yearly_earnings=1.18e+07.
- category=Sports: mean highest_yearly_earnings=9.62e+06.
- category=Pets & Animals: mean highest_yearly_earnings=9.58e+06.

## Limitations

- High-missingness columns require an explicit imputation policy.
- Estimated manual effort and value are heuristics pending customer calibration.

## Reproduce

```bash
avaloka analyze app/sample_data/Global_YouTube_Statistics.csv --goal 'average highest_yearly_earnings by category' --output ./reproduced-analysis
```

---
_Reproduce or adapt this mission with `avaloka`._