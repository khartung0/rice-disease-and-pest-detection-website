# Downloads and provenance

**Release `engineering-v1` · 2026-09-30 · D003 validation engineering check.**

| File | Contents |
|---|---|
| [Results JSON](assets/publications/engineering-v1/results.json) | Full-precision metrics, confusion matrix, training history, and run setup |
| [Provenance JSON](assets/publications/engineering-v1/provenance.json) | Source-file and generator SHA-256 hashes; code fingerprint |

Both documents use schema version 1. Class arrays define confusion-matrix order: rows are
recorded labels, columns are predictions. Support is an image count; JSON epochs are zero-based.
The results page rounds scores to three decimals.

Reproduce the tables with `python scripts/render_publication.py` in the public website repo.
Full training reproduction also requires the private experiment code/configuration and source
dataset; these downloads alone are not a training package. The run recorded uncommitted code
changes, identified by its saved code fingerprint.

No images, image IDs, individual predictions, raw manifests, machine paths, or test results are
included. Source images retain their original terms; this release grants no image redistribution
rights. Identify the release ID and hashes when referring to these results.

## File checksums (SHA-256)

```text
results.json  e2745c8b376e8e05d7c42454cf6f14b4471dd11bbd2c60e71156863664c8b24e
provenance.json  7320004cc5edae4d190a7ecf8b1c6466010ea751e12ddc22071b49adb03d7f5a
```

Try the [student exercises](learning.md) using these files.
