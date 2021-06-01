# Spam-Page-Detection

## M151: Web Systems and Information Retrieval

### Abstract

In this work we create a classification model to identify Spam Pages based on their *URL*. In order to achieve that, we've selected the most "meaningful" features from the ones existing in ISCXURL2016 dataset. We evaluate our selection by performing a 10-fold Cross Validation for various classifiers as well as datasets. We've also implemented a simple Flask App, to vizualise our results.

### Dataset

ISCXURL2016 Final Spam dataset: Contains the features extracted by various spam & benign URLS. This dataset has in total 80 columns: 79 feature columns and 1 label column.

ISCXURL2016 Spam URL dataset: Contains spam URLS.

ISCXURL2016 Benign URL dataset: Contains benign URLS.### Feature selection

### Feature selection

In order to keep the most important features, we've created two sets of featues. The first one contained the ones that are highly correlated (with threashold = 0.85) and the second one, the low score features resulted from k-best features algorithm (where k=35). The union of those two sets produced a large set which contained 62 features. These features were removed.

The selected features are the following:
```
- domain token count
- average domain token length
- digit letter digit pattern count url
- domain length
- argument - url ratio
- number of dots in url
- character continuity rate
- url queries variable
- delimiter count path
- number rate url
- number rate filename
- number rate extension
- number rate afterpath
- symbol count url
- symbol count filename
- entropy domain
- entropy extension
```

We've created a new dataset by appending and shuffling ISCXURL2016 Spam & Benign URL datasets. From this dataset we've computed the 17 features mentioned above.


### Classifier selection

We've tested the reliability of this selection by performing a 10-Fold Cross Validation with various classifiers.
```

Results of ISCXURL2016 Final Spam dataset

|     Classifier    |  Mean F1 - Score  |
-----------------------------------------
| bagging-dtree     |       0.997       |
| decision-tree     |       0.995       |     
| knn               |       0.994       |
| logisticreg       |       0.986       |
| naive-bayes       |       0.941       |
| random-forest     |       0.998       |
| linear-svc        |       0.988       |
| voting-classifier |       0.988       |

Results of Benign+Spam dataset

|     Classifier    |  Mean F1 - Score  |
-----------------------------------------
| bagging-dtree     |       0.997       |
| decision-tree     |       0.995       |     
| knn               |       0.994       |
| logisticreg       |       0.986       |
| naive-bayes       |       0.941       |
| random-forest     |       0.998       |
| linear-svc        |       0.988       |
| voting-classifier |       0.988       |

```
We've selected Random Forest as the most suitable classifier for this problem as it achieved the highest score in both cases.

### Code

Feature Exploration, Classification & Feature Selection are implemented in Spam_Page_Detection.ipynb.

### Application

#### Run

```
$ export FLASK_APP=flaskapp/__init__.py
$ python -m flask run
```

### Authors

George Panagiotopoulos
Maria Despoina Siampou

