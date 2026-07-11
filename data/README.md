# Data note

The large raw NOAA/NCEI IBTrACS North Atlantic CSV is not committed. Download the Version 4r01 `NA` subset from the official IBTrACS page, rename it to `ibtracs_NA.csv`, and place it in the repository root when rebuilding the data pipeline.

The archived raw source used by this project had SHA-256:

```text
9df93cf1908027c18c0d7ffd701bf62870bb71254a833f6ebec567f2cc87dd75
```

The minimum processed inputs remain at repository root because the current notebooks resolve files relative to `Path.cwd()`.

The included event-node dataset is derived from the project study window and the 200 km / 50 kt exposure-proxy rule. See [`../DATA_SOURCES.md`](../DATA_SOURCES.md) for provenance, attribution, version notes, limitations, and recommended citations.
