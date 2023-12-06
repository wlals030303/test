import pandas as pd

obs = [22,19,26,25,17,11]
exp = [20,20,20,20,20,20]

from scipy.stats import chisquare

result = chisquare(obs,exp)
print(result)
print()

obs = pd.DataFrame({'남':[26,20,11],'여':[10,15,18]})
obs.index=['만족','보통','불만족']

from scipy.stats import chi2_contingency

result = chi2_contingency(obs,correction=False)
print(result)
print()

obs = pd.DataFrame({'남':[26,75],'여':[45,55]})
obs.index=['찬성','반대']
result = chi2_contingency(obs, correction=False)
print(result)
print()


