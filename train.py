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
    result = predict('http://paypal.com.webscr.cmd.login.submit.dispatch.5885d80a13c0db1f8e263663d3faee8db2b24f7b84f1819343fd6c338b1d9d.222studio.com/UK/')
    print(result)
