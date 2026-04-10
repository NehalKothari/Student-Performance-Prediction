import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def load_model():
    df = pd.read_csv("data/student-mat.csv", sep=';')

    df = df[['studytime', 'failures', 'absences',
             'health', 'freetime', 'goout',
             'G1', 'G2', 'G3']]

    X = df.drop('G3', axis=1)
    y = df['G3']

    model = DecisionTreeRegressor(max_depth=5)
    model.fit(X, y)

    return model

def predict(model, input_data):
    return model.predict([input_data])[0]