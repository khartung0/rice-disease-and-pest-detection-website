# Data and task

The first experiment uses an eight-class disease subset of **Paddy Doctor**, distributed through
the [Paddy Disease Classification competition](https://www.kaggle.com/competitions/paddy-disease-classification/data).
It is close-range rice imagery, not a sample of all agricultural settings or aerial views.

| Included label | Meaning in this task |
|---|---|
| `normal` | Recorded healthy/normal class |
| `bacterial_leaf_blight`, `bacterial_leaf_streak`, `bacterial_panicle_blight` | Three bacterial disease labels |
| `blast`, `brown_spot`, `downy_mildew`, `tungro` | Four further disease labels |

`hispa` and `dead_heart` are excluded because they are pest-related categories. Labels are
annotations, not independently confirmed diagnoses for every image.

D003 uses **5,148 training images and 1,113 validation images** from `disease_split_v2`.
Validation class counts accompany the results. Near-duplicate photos are grouped before
splitting, so related images do not cross train/validation/test boundaries.

**Limits:** single-source evidence, uneven class counts, and unresolved label conflicts.
Independent field evaluation is needed before wider generalization claims. Raw images are not
redistributed; obtain them under the source's access and licence terms. Availability alone
does not establish permission for deployment or redistribution.
