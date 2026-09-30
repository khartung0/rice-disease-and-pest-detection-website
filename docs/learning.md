# A short guide for students

Read the [results](results.md), then use the [aggregate downloads](downloads.md) to check what
the numbers mean. No GPU or image dataset is needed for these exercises.

| Term | What to look for |
|---|---|
| Classification | One recorded disease/normal label per image |
| Precision | Of predictions for a class, how many have that recorded label? |
| Recall | Of images with a recorded class label, how many were found? |
| F1 | Harmonic mean of precision and recall |
| Macro-F1 | Mean F1 across classes, giving rare classes equal weight |
| Support | Number of validation images with that recorded label |
| Confusion matrix | Rows are recorded labels; columns are predictions |
| Generalization | Performance on data beyond the training conditions |

## Try three checks

1. Sum per-class support: it should total **1,113**. Check that each confusion-matrix row
   has the same sum as its class support.
2. Divide the diagonal sum by 1,113 to reproduce accuracy. Average the eight class F1
   values to reproduce macro-F1. Why do these numbers differ?
3. Compare per-image and cluster-weighted macro-F1. What extra information would explain
   the difference? Aggregate metrics alone cannot identify causes of disease.

**Discussion:** would this justify deployment in another region or on drone images?
Describe the additional data and evaluation you would request.
