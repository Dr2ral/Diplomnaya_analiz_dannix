import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("files/Churn_Modelling.csv")
sns.scatterplot(x='Gender', y='Balance', data=data)
plt.show()
