# Preliminary results

**D003 · engineering check · validation only · release engineering-v1.**

This two-epoch ResNet18 run checks the pipeline on split v2. It is not a model
selection result, a measure of field readiness, or a comparison with a published benchmark.

Training: **5,148 images**; validation: **1,113 images**; seed **42**.
Metrics come from epoch **2 of 2** (stored index 1).

| Validation metric | Value |
|---|---:|
| Macro-F1, per image | 0.862 |
| Accuracy | 0.877 |
| Macro-F1, cluster-weighted | 0.877 |

## Where performance differs

| Recorded class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| bacterial leaf blight | 0.689 | 0.680 | 0.685 | 75 |
| downy mildew | 0.798 | 0.781 | 0.789 | 96 |
| brown spot | 0.931 | 0.745 | 0.828 | 145 |
| tungro | 0.892 | 0.865 | 0.879 | 163 |
| blast | 0.867 | 0.927 | 0.896 | 261 |
| bacterial leaf streak | 0.980 | 0.862 | 0.917 | 58 |
| normal | 0.902 | 0.977 | 0.938 | 265 |
| bacterial panicle blight | 0.926 | 1.000 | 0.962 | 50 |

Bacterial leaf blight has the lowest F1 in this run. Higher cluster-weighted
macro-F1 shows that repeated photographs affect the summary; it does not explain why
the model made those errors.

## Training progress

| Epoch (1-based) | Train loss | Validation loss | Validation macro-F1 |
|---|---:|---:|---:|
| 1 | 0.899 | 0.553 | 0.798 |
| 2 | 0.447 | 0.426 | 0.862 |

**Limits:** one seed, two epochs, one source, unresolved label conflicts, and no
independent field evaluation. A different split is not a comparable model benchmark.

See [Methods](approach.md) for the protocol and [Downloads](downloads.md) for full-precision
metrics, the confusion matrix, and source hashes. Interactive charts are a later addition.
