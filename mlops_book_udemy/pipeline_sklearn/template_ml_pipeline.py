from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric_features = ["age", "balance"]
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

categorical_features = [
    "job",
    "marital",
    "education",
    "contact",
    "housing",
    "loan",
    "default",
    "day",
]
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


# Add classifier to the preprocessing pipeline
clf_pipeline = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)

# clf_pipeline.fit(X_train, y_train)

# Custom transformer


class AddToColumsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, addition=0.0, columns=None):
        self.addition = addition
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        transform_columns = list(X.columns)
        if self.columns:
            transform_columns = self.columns
        X[transform_columns] = X[transform_columns] + self.addition
        return X
