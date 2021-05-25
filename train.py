from feature_extraction import URL
import pandas as pd
import pickle

# load URL
url = URL('http://google.com')

# extract features from URL
data = url.feature_extraction()
X_test = pd.DataFrame(data)

# predict label 
with open(r"train.pickle", "rb") as input_file:
  model = pickle.load(input_file)
  y = model.predict(X_test)
  print(y)
