#SVR
# Importing the dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = y.reshape(len(y),1) #shows you have that thing, keep going
y = sc_y.fit_transform(y)


from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)# Fitting the SVR Model to the data

# Create your regressor here

# Predicting a new result
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
'''what we did in above line is used regressor.predict to predict o/p but since X is 
scaled so used sc_X.transform on inspecting it(ctrl+I) we got that we need to convert it into an
array so used np.array and put 2[[]] as it 2-d array, After this we inversed it as it was scaled in 
X so used sc_y.inverse_transform'''
# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
