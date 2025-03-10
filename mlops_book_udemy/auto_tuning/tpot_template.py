from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, train_size=0.75, test_size=0.25, random_state=42
)

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export("tpot_digits_pipeline.py")
