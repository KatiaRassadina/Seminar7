import numpy as np
import scipy.stats as stats
import warnings
warnings.filterwarnings("ignore")

x1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

stats.kruskal(x1, x2, x3)
KruskalResult(statistic=5.465564058257224, pvalue=0.0650380998590494)
#pvalue > alpha, H0 - не отвергается с ошибкой alpha = 0.05, различий нет, группы статистически равны