from feature_extraction import URL
import pandas as pd
import pickle


def predict(given_url):
    # load URL
    url = URL(given_url)

    # extract features from URL
    data = url.feature_extraction()
    X_test = pd.DataFrame(data)

    # predict label
    with open(r"train.pickle", "rb") as input_file:
        model = pickle.load(input_file)
        y = model.predict(X_test)
        return y[0]


if __name__ == '__main__':
    result = predict('https://www.google.com/calendar/embed?showTitle=0&height=600&wkst=1&bgcolor=%23FFFFFF&src=qtbqjvhotpcmi2gbkhp15bbh7s@group.calendar.google.com&color=%235C1158&ctz=America/New_York')
    print(result)
