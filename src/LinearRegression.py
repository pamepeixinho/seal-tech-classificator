import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn import tree

pkl_filename = "pickle_model.pkl"

def commitmentTrain():
    df = pd.read_csv('out.csv')
    class_eng = df.values

    print(class_eng)

    X = class_eng[:, 1:]  # select columns 1 through end
    y = class_eng[:, 0]  # select column 0, the stock price

    class_eng_X_train = X[:-20]
    class_eng_X_test = X[-20:]

    class_eng_y_train = y[:-20]
    class_eng_y_test = y[-20:]

    clf = tree.DecisionTreeRegressor()

    clf = clf.fit(X, y)


    # with open(pkl_filename, 'wb') as file:
    #     pickle.dump(regr, file)

    print(class_eng_X_test)

    class_eng_y_pred = clf.predict(class_eng_X_test)
    # print(class_eng_y_pred)

    # print("Mean squared error: %.2f"
    #       % mean_squared_error(class_eng_y_test, class_eng_y_pred))
    # print('Variance score: %.2f' % r2_score(class_eng_y_test, class_eng_y_pred))

    # Plot outputs
    # plt.scatter(class_eng_X_test, class_eng_y_test,  color='black')
    # plt.plot(class_eng_X_test, class_eng_y_pred, color='blue', linewidth=3)
    #
    # plt.xticks(())
    # plt.yticks(())
    #
    # plt.show()


def predict(emotions):
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
        pickle_model.predict(emotions)

commitmentTrain()
