import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("dataset_part_3.csv")
X = pd.get_dummies(df.drop(columns=["Class"]), drop_first=True)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2, stratify=y
)

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=2),
    {"criterion": ["gini", "entropy"], "max_depth": [2, 4, 6, 8]},
    cv=10,
)
grid.fit(X_train, y_train)

predictions = grid.predict(X_test)
print("Best parameters:", grid.best_params_)
print("Test accuracy:", accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
