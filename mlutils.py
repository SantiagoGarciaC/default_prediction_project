from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

def plot_learning_curve(estimator,X,y,cv): 
  train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, shuffle=True)
  train_scores_mean = np.mean(train_scores, axis=1)
  train_scores_std = np.std(train_scores, axis=1)
  test_scores_mean = np.mean(test_scores, axis=1)
  test_scores_std = np.std(test_scores, axis=1)
  # Plot learning curve
  plt.grid()
  plt.fill_between(
          train_sizes,
          train_scores_mean - train_scores_std,
          train_scores_mean + train_scores_std,
          alpha=0.1,
          color="r",
      )
  plt.fill_between(
          train_sizes,
          test_scores_mean - test_scores_std,
          test_scores_mean + test_scores_std,
          alpha=0.1,
          color="g",
      )
  plt.plot(train_sizes, train_scores_mean, "o-", color="r", label="train score")
  plt.plot(train_sizes, test_scores_mean, "o-", color="g", label="test score")
  plt.legend(loc="best")
  plt.ylabel("Score")
  plt.xlabel("Training examples")
  plt.title(estimator.__class__.__name__)
  return plt.show()