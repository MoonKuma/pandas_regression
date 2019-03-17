# Pandas_regression
#### Abstract

​	A test project targeting on trying various model on regression problems.

#### Models

##### General linear models

- Linear regression

  - ```python
    from sklearn.linear_model import LinearRegression
    
    model = LinearRegression()
    ```

- Ridged regression 

  - Adding penalty in least squares

  - ```python
    from sklearn import linear_model
    
    reg = linear_model.Ridge(alpha=.5) # aplha is the coefficient of penalty
    ```

- Least-angle regression (LARS)

  - suitable when the number of dimensions is significantly greater than the number of points

  - ```python
    from sklearn import linear_model
    
    reg = linear_model.LassoLars(alpha=.1)
    ```

- Bayesian Ridge Regression

  - Adjust in a at-hand way

  - ```python
    from sklearn import linear_model
     
    reg = linear_model.BayesianRidge()
    ```

##### Kernel

- Support vector regression

  - ```python
    from sklearn.svm import SVR
    
    svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
    svr_lin = SVR(kernel='linear', C=100, gamma='auto')
    svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
                   coef0=1)
    ```

- Gaussian process regression
  - The prediction is probabilistic (Gaussian) so that one can compute empirical confidence intervals

  -  different kernels can be specified 

  - ```python
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, WhiteKernel
    
    kernel = 1.0 * RBF(length_scale=100.0, length_scale_bounds=(1e-2, 1e3)) \
        + WhiteKernel(noise_level=1, noise_level_bounds=(1e-10, 1e+1))
    gp = GaussianProcessRegressor(kernel=kernel,alpha=0.0)
    ```

##### Nearest neighbors

- K neighbors regression

  - ```python
    from sklearn import neighbors
    
    n_neighbors = 5
    weights = 'uniform'
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    ```

##### Decision tree

- Decision tree

  - ```python
    from sklearn import tree
    
    clf = tree.DecisionTreeRegressor()
    ```

##### Ensemble method

- RandomForest

  - ```python
    from sklearn.ensemble import RandomForestRegressor
    
    max_depth=100
    n_estimators=1000
    max_features=1
    
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators, max_features=max_features)
    ```

- Gradient Boosted Regression Trees

  - Natural handling of data of mixed type (= heterogeneous features)

  - Predictive power

  - Robustness to outliers in output space (via robust loss functions)

  - ```
    from sklearn.ensemble import GradientBoostingRegressor
    
    est = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,max_depth=1, random_state=0, loss='ls')
    ```

##### Neural network

- Deep neural network 
  - The (simplest) neural network model

  - The activation function of the last layer is usually set to 'identity' for regression problems, but here we set it to 'Relu' because there ought to have no negative questionnaire scores

  - ```python
    from sklearn.neural_network import MLPRegressor
    
    clf = MLPRegressor(hidden_layer_sizes=(100, ), activation=’relu’, solver=’adam’, alpha=0.0001, batch_size=’auto’, learning_rate=’constant’, learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)
    ```


#### Environment

- Python 3.6 (Anaconda)
  - numpy, sklearn, plt,pandas and other related packages
  - update sklearn into v20.0 is not mandatory (but may be helpful XD) 
- Tensor1.6
  - for building neural network models