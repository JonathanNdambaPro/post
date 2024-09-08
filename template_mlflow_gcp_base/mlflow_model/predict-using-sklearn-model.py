import mlflow
import numpy as np

mlflow.set_tracking_uri("http://127.0.0.1:8080")
logged_model = "runs:/85bd0ddbbef14982a0735246f7c9f1be/model"
loaded_model = mlflow.pyfunc.load_model(logged_model)
random_data = np.random.randn(1, 87931)
prediction = loaded_model.predict(random_data)
print(prediction)
