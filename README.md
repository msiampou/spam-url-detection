# Spam-Page-Detection

## M151: Web Systems and Information Retrieval

### Abstract

In this work we create a classification model to identify Spam Pages based on their *URL*. ISCXURL2016 dataset, contains 79 features extracted from various benign and spam URLs. However, having a large number of features may lead overfitting, or consume extra time to compute unecessary features. For that reason, we performed a feature exploration and chose to use only the most "meaningful" features. To evaluate our selection, we've performed a Cross Validation for various classifiers. Finally, we've implemented a simple Flask App, where a user can insert a URL to find out if it is spam or not.

### Datasets

ISCXURL2016 Final Spam dataset: Contains the features extracted by various spam & benign URLS. This dataset has 80 columns in total: 79 feature columns and 1 label column.

Spam URL dataset: Contains spam URLS.

Benign URL dataset: Contains benign URLS.

Spam+Benign URL dataset: A concatenation of Spam & Benign URL datasets. 

### Feature selection

In order to keep the most important features, we've created two sets of featues. The first one contained the ones that are highly correlated (with threashold = 0.85) and the second one, the low score features resulted from k-best algorithm (where k=35). The union of those two sets produced a large set which contained 62 features. These features were removed.

The selected features are the following:
```
- Token count in domain
- Average token length in domain
- Digit Letter Digit count in URL
- Domain length
- Argument-URL ratio
- Number of dots in URL
- Character continuity rate in URL
- Length of URL query variable
- Delimiter count in path
- Number rate in URL
- Number rate in filename
- Number rate in extension
- Number rate in afterpath
- Symbol count in URL
- Symbol count in filename
- Alphabet Entropy of domain
- Alphabet Entropy of extension
```

After selecting these 17 features we modified our two main dataset as follows:
```
- ISCXURL2016 Final Spam dataset: Only these 17 features were kept.
- Spam+Benign URL dataset: The 17 features were extracted from the URLS. The URL column was then dropped.
```

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
| bagging-dtree     |       0.999       |
| decision-tree     |       0.998       |     
| knn               |       0.948       |
| logisticreg       |       0.972       |
| naive-bayes       |       0.901       |
| random-forest     |       0.999       |
| linear-svc        |       0.948       |
| voting-classifier |       0.978       |

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

#### Implementation Details

Having a trained model, our application receives a URL and outputs whether this URL is spam or not. Our model is trained on ISCXURL2016 Final Spam dataset, using Random Forest.

#### Code
The implementation of our application lies under app/ folder.

### Presentation

You can find a mini presentation of our project in pres/ folder 

### Authors

George Panagiotopoulos (cs219...)
Maria Despoina Siampou (cs220017)

