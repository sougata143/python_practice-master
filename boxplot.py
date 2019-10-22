import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')
plt.plot(df)
plt.show()
# print(df)