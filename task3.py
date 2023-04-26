import numpy as np
import scipy.stats as stats
import warnings
warnings.filterwarnings("ignore")

x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])
alpha=0.05
stats.wilcoxon(x1, x2)
WilcoxonResult(statistic=0.0, pvalue=0.0625)
#Cтатистически значимых различий не обнаружено на уровне значимости alpha = 0.05.