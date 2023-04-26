import numpy as np
import scipy.stats as stats
import warnings
warnings.filterwarnings("ignore")

x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
x3 = np.array([130, 130, 120, 130, 125])

stats.friedmanchisquare(x1, x2, x3)
FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)
#pvalue < alpha, H0 - отвергается с ошибкой alpha = 0.05, принимается гипотиза Н1 - различия есть. Препарат работает.