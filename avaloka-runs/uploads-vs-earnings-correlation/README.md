# Avaloka mission `a7c4ae978dc3`

**Goal:** correlation between uploads and highest_yearly_earnings

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

- uploads and highest_yearly_earnings: Pearson r=0.167.
- Correlation alone does not establish causation.

## Limitations

- High-missingness columns require an explicit imputation policy.
- Estimated manual effort and value are heuristics pending customer calibration.

## Reproduce

```bash
avaloka analyze app/sample_data/Global_YouTube_Statistics.csv --goal 'correlation between uploads and highest_yearly_earnings' --output ./reproduced-analysis
```

---
_Reproduce or adapt this mission with `avaloka`._