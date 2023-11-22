import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# df = pd.read_excel("이원분석_주행거리.xlsx", engine='openpyxl')
# model = ols('distance ~ C(road) + C(car)',data=df).fit()
# print(anova_lm(model),'\n')

# from statsmodels.stats.multicomp import pairwise_tukeyhsd
# tukey = pairwise_tukeyhsd(df['distance'],df['road'],alpha=0.05)
# print(tukey,'\n')

# tukey = pairwise_tukeyhsd(df['distance'],df['car'],alpha=0.05)
# print(tukey,'\n')

df = pd.read_excel("화장품_매출액.xlsx", engine='openpyxl')
df.columns = ['area', 'service', 'sales']

model = ols('sales ~ C(area) + C(service) + C(area):C(service)',data=df).fit()
print(anova_lm(model),'\n')

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(df['sales'],df['area'],alpha=0.05)
print(tukey,'\n')

tukey = pairwise_tukeyhsd(df['sales'],df['service'],alpha=0.05)
print(tukey,'\n')
