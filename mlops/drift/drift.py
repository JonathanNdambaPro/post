from alibi_detect.cd import TabularDrift
from evidently.metric_preset import DataDriftPreset
from evidently.report import Report
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine_data = load_wine()
feature_names = wine_data.feature_names
X, y = wine_data.data, wine_data.target
X_ref, X_test, y_ref, y_test = train_test_split(X, y, test_size=0.50, random_state=42)

# DataDrift
cd = TabularDrift(x_ref=X_ref, p_val=0.05)

preds = cd.predict(X_test)
labels = ["No", "Yes"]
print("Drift: {}".format(labels[preds["data"]["is_drift"]]))

X_test_cal_error = 1.1 * X_test
preds = cd.predict(X_test_cal_error)
labels = ["No", "Yes"]
print("Drift: {}".format(labels[preds["data"]["is_drift"]]))


cd = TabularDrift(x_ref=y_ref, p_val=0.05)

preds = cd.predict(y_test)
labels = ["No", "Yes"]
print("Drift: {}".format(labels[preds["data"]["is_drift"]]))

y_test_cal_error = 1.1 * y_test
preds = cd.predict(y_test_cal_error)
labels = ["No", "Yes"]
print("Drift: {}".format(labels[preds["data"]["is_drift"]]))


# ConceptDrift
# from alibi_detect.cd import MMDDriftOnline
# ert = 50
# window_size = 10
# cd = MMDDriftOnline(X_ref, ert, window_size, backend='pytorch',
#                     n_bootstraps=2500)

# cd.predict(X)['data'] ['is_drift']

## Une bonne astuce pour détecter les variables à surveiller est d'utiliser features importance avec un random forest

# import pandas as pd
# feature_names = rf[:-1].get_feature_names_out()
# mdi_importances = pd.Series(rf[-1].feature_importances_,
#                             index=feature_names).sort_values(ascending=True)

## On peut aussi utiliser permutation_importance

# from sklearn.inspection import permutation_importance
# result = permutation_importance(
#     rf, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
#     )
# sorted_importances_idx = result.importances_mean.argsort()
# importances = pd.DataFrame(
#     result.importances[sorted_importances_idx].T,
#     columns=X.columns[sorted_importances_idx])


## Ou shap Value
# import shap

# explainer = shap.Explainer(rf, predict, X_test)
# shap_values = explainer(X_test)
# shap.plots.bar(shap_values)


wine_data = load_wine(as_frame=True)
feature_names = wine_data.feature_names
X, y = wine_data.data, wine_data.target

X_ref, X_test, y_ref, y_test = train_test_split(X, y, test_size=0.50, random_state=42)

data_drift_report = Report(metrics=[DataDriftPreset()])
data_drift_report.run(reference_data=X_ref, current_data=X_test)

data_drift_report.save_json("data_drift_report.json")
data_drift_report.save_html("data_drift_report.html")
