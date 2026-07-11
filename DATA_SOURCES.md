# Data sources and provenance

## Primary public data source

This project uses the **International Best Track Archive for Climate Stewardship (IBTrACS)**, a unified public tropical-cyclone best-track dataset maintained by the **NOAA National Centers for Environmental Information (NCEI)**.

| Item | Recorded information |
|---|---|
| Dataset | International Best Track Archive for Climate Stewardship (IBTrACS) |
| Release | Version 4r01 |
| Subset | North Atlantic basin (`NA`) |
| Provider | NOAA National Centers for Environmental Information |
| DOI | `10.25921/82ty-9e16` |
| Official page | https://www.ncei.noaa.gov/products/international-best-track-archive |
| Local normalized filename | `ibtracs_NA.csv` |
| Archived file timestamp | 2026-05-29 11:54:02 |
| Archived file size | 57,074,222 bytes |
| Archived file SHA-256 | `9df93cf1908027c18c0d7ffd701bf62870bb71254a833f6ebec567f2cc87dd75` |

The source filename was normalized to `ibtracs_NA.csv`, so the original upstream filename is no longer preserved. Version 4r01 is the NOAA release documented for this project. The access date used in the citation is May 29, 2026, based on the archived file timestamp. For a formal publication, replace it only if a more precise original download record is recovered.

The SHA-256 fingerprint was computed from the raw CSV stored in the original project archive. It allows an exact-file comparison without redistributing the 57 MB source file.

## Redistribution policy

The raw IBTrACS North Atlantic CSV is not included in the public repository. This avoids duplicating a large, actively maintained source dataset and directs users to the authoritative NOAA/NCEI copy.

The `.gitignore` file explicitly excludes:

```text
ibtracs_NA.csv
```

Processed and derived files included in the repository are products of the author's analysis. Their inclusion does not transfer ownership of the underlying IBTrACS observations.

## Processing performed in this project

The raw storm-track observations are transformed into a decision-focused event-node dataset by:

1. retaining the study-period North Atlantic events used by the project;
2. associating hurricane events with 14 geographically grounded supply-chain nodes;
3. computing storm-to-node proximity and intensity-based features;
4. defining exposure using a 200 km distance threshold and a 50 kt wind threshold;
5. constructing 6,496 event-node observations from 464 events and 14 nodes;
6. estimating calibrated scenario-conditioned risk representations;
7. reducing the scenario set for optimization and validating decisions on the full 464-scenario set.

The resulting target is a **hazard-exposure proxy**. It should not be interpreted as direct evidence of facility closure, inventory loss, transport interruption, or realized company-level disruption.

## Files derived from or linked to the public data

- `storm_node_dataset_14nodes_200km_50kt.csv`
- `final_risk_predictions_oof_without_season.csv`
- `final_scenario_node_probabilities_full_without_season.csv`
- `final_hybrid_reduced_hurricane_scenarios_without_season.csv`
- `final_optimization_scenario_node_risk_matrix_without_season.csv`
- result tables and figures under `results/`

The supply-chain node, transport-arc, and optimization-parameter files describe the stylized testbed used in this research and are not part of the IBTrACS dataset.

## Rebuilding from the official source

1. Visit the official NOAA/NCEI IBTrACS page.
2. Download the Version 4r01 North Atlantic CSV subset.
3. Rename the file to `ibtracs_NA.csv`.
4. Place it in the repository root.
5. Run `01_data_and_ml_pipeline.ipynb` from the repository root.
6. To check whether a downloaded file exactly matches the archived source used in this project, calculate its SHA-256 and compare it with the fingerprint above.

Because IBTrACS is updated regularly, a newly downloaded file may contain revisions or additional recent storms. The processed datasets and saved result files in this repository are therefore the appropriate reference for inspecting the reported public results.

## Recommended citations

Gahtan, J., K. R. Knapp, C. J. Schreck, H. J. Diamond, J. P. Kossin, and M. C. Kruk (2024). *International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4r01, North Atlantic subset*. NOAA National Centers for Environmental Information. DOI: `10.25921/82ty-9e16`. Accessed May 29, 2026 (date recorded from archived source-file metadata).

Knapp, K. R., M. C. Kruk, D. H. Levinson, H. J. Diamond, and C. J. Neumann (2010). “The International Best Track Archive for Climate Stewardship (IBTrACS): Unifying Tropical Cyclone Best Track Data.” *Bulletin of the American Meteorological Society*, 91, 363–376. DOI: `10.1175/2009BAMS2755.1`.
