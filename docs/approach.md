# Methods

The published example asks whether the training/evaluation pipeline works on a representative
split. It does not select a winning model.

| D003 setup | Value |
|---|---|
| Model | ResNet18, ImageNet pretrained, eight-class output |
| Input | 224 x 224 RGB |
| Optimizer | AdamW; learning rate 0.0001; batch size 8 |
| Training | Two epochs; seed 42 |
| Augmentation | Random crop and horizontal flip during training only |
| Selection | Best validation macro-F1 |

**Split before training.** Near-duplicate clusters stay together. Split v2 includes repeated
scenes in validation rather than evaluating only one-off photographs.

**Keep the test split locked.** Validation guides choices; final test evaluation comes after
selection is frozen. This release contains validation results only.

**Use complementary metrics.** Macro-F1 gives every class equal weight. Per-class scores and
support reveal failures hidden by overall accuracy. Cluster-weighted metrics give each
near-duplicate group total weight one, reducing the influence of repeated photographs.

**Keep claims traceable.** Saved aggregates generate the public tables. Downloadable provenance
identifies the exact inputs by SHA-256. One seed and two epochs establish neither convergence
nor uncertainty across repeated training.
