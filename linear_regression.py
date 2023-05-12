from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([1, 2, 3]).reshape(-1, 1)
y = np.array([2, 3, 5])

model = LinearRegression()

model.fit(X, y)

hours = np.array([3]).reshape(-1, 1)
predicted_scores = model.predict(hours)

print(predicted_scores)
