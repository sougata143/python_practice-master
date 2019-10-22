from scipy.stats import binom
import seaborn as sb

binom.rvs(size=10,n=20,p=0.8)

data_binom = binom.rvs(n=20,p=0.8,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')

# import seaborn as sns, numpy as np
# import pandas as pd
# from scipy.stats import norm


# sns.set(); np.random.seed(0)
# x = np.random.randn(100)
# ax = sns.distplot(x)
# x = pd.Series(x, name="x variable")
# ax = sns.distplot(x)
# ax = sns.distplot(x, rug=True, hist=False)
# ax = sns.distplot(x, fit=norm, kde=False)
# ax = sns.distplot(x, vertical=True)
# sns.set_color_codes()
# ax = sns.distplot(x, color="y")
# ax = sns.distplot(x, rug=True, rug_kws={"color": "g"},
#                    kde_kws={"color": "k", "lw": 3, "label": "KDE"},
#                    hist_kws={"histtype": "step", "linewidth": 3,
#                              "alpha": 1, "color": "g"})