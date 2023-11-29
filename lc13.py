import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols

df = pd.DataFrame(pd.read_excel("Galtons Height Data_딸.xlsx",engine='openpyxl'))
df = 2.54 * df

sns.regplot(x=df.father, y= df.daughter)
plt.show()

res = ols('df.daughter ~ df.father', data=df).fit()
print(res.summary())