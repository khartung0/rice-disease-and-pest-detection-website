"""Generate concise public tables and downloads from a selected aggregate release."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def render(root=ROOT):
    release = json.loads((root / "publication.json").read_text(encoding="utf-8"))["release_id"]
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", release):
        raise ValueError("Invalid release ID")
    bundle = root / "publications" / release
    payloads = {name: (bundle / name).read_bytes() for name in ("results.json", "provenance.json")}
    data, provenance = (json.loads(payloads[name]) for name in ("results.json", "provenance.json"))
    if any(d.get("schema_version") != 1 or d.get("release_id") != release for d in (data, provenance)):
        raise ValueError("Publication schema/release mismatch")
    run = data["run"]
    if (run["experiment_id"] != "D003_resnet18_smoke_split_v2"
            or run["purpose"] != "engineering_check" or run["split"] != "val"):
        raise ValueError("This first page template supports D003 engineering validation only")
    def label(value):
        if not re.fullmatch(r"[A-Za-z0-9_ -]+", value):
            raise ValueError("Unexpected label characters")
        return value.replace("_", " ")
    scores = run["metrics"]
    lines = ["# Preliminary results", "",
        f"**D003 · engineering check · validation only · release {release}.**", "",
        "This two-epoch ResNet18 run checks the pipeline on split v2. It is not a model",
        "selection result, a measure of field readiness, or a comparison with a published benchmark.", "",
        f"Training: **{run['n_train']:,} images**; validation: **{run['n_val']:,} images**; seed **{run['seed']}**.",
        f"Metrics come from epoch **{run['best_epoch'] + 1} of {run['epochs']}** (stored index {run['best_epoch']}).", "",
        "| Validation metric | Value |", "|---|---:|",
        f"| Macro-F1, per image | {scores['macro_f1']:.3f} |",
        f"| Accuracy | {scores['accuracy']:.3f} |",
        f"| Macro-F1, cluster-weighted | {scores['cluster_weighted_macro_f1']:.3f} |", "",
        "## Where performance differs", "",
        "| Recorded class | Precision | Recall | F1 | Support |", "|---|---:|---:|---:|---:|"]
    for p in sorted(run["per_class"], key=lambda p: p["f1"]):
        lines.append(f"| {label(p['label'])} | {p['precision']:.3f} | {p['recall']:.3f} | {p['f1']:.3f} | {p['support']} |")
    lines += ["", "Bacterial leaf blight has the lowest F1 in this run. Higher cluster-weighted",
        "macro-F1 shows that repeated photographs affect the summary; it does not explain why",
        "the model made those errors.", "", "## Training progress", "",
        "| Epoch (1-based) | Train loss | Validation loss | Validation macro-F1 |", "|---|---:|---:|---:|"]
    for h in run["history"]:
        lines.append(f"| {h['epoch'] + 1} | {h['train_loss']:.3f} | {h['val_loss']:.3f} | {h['val_macro_f1']:.3f} |")
    lines += ["", "**Limits:** one seed, two epochs, one source, unresolved label conflicts, and no",
        "independent field evaluation. A different split is not a comparable model benchmark.", "",
        "See [Methods](approach.md) for the protocol and [Downloads](downloads.md) for full-precision",
        "metrics, the confusion matrix, and source hashes. Interactive charts are a later addition.", ""]
    (root / "docs/results.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    destination = root / "docs/assets/publications" / release
    destination.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items():
        (destination / name).write_bytes(payload)
    checksums = "\n".join(f"{name}  {hashlib.sha256(payload).hexdigest()}" for name, payload in payloads.items())
    downloads = f"""# Downloads and provenance

**Release `{release}` · {data['publication_date']} · D003 validation engineering check.**

| File | Contents |
|---|---|
| [Results JSON](assets/publications/{release}/results.json) | Full-precision metrics, confusion matrix, training history, and run setup |
| [Provenance JSON](assets/publications/{release}/provenance.json) | Source-file and generator SHA-256 hashes; code fingerprint |

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
{checksums}
```
"""
    (root / "docs/downloads.md").write_text(downloads, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    render()
