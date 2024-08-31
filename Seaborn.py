import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("files/Churn_Modelling.csv")

'''В данном графике мы расматриваем отношение баланса к возрасту по странам'''
samp = data.sample(n=50) # Использую для удобочитаемоести
#sns.scatterplot(data=samp, x='Age', y='Balance', hue='Geography',
#                palette=['red', 'green', 'blue'], s=100)

'''Визуализация зависимости времени пользования услуг клиентами по странам '''
#sns.catplot(x='Geography', kind='count', hue='Tenure', data=data, palette='dark:r')

'''Визуализируем зависимость баланса от возраста и добавляем разбиение по полу'''
#sns.relplot(data=samp, x="Balance", y="Age", kind="line", hue='Gender')

'''Визуализация соотношения количества клиентов в странах с разбиением по полу, методом "histplot" '''
sns.histplot(data=data, x='Geography', hue='Gender')

'''Визуализация гистограммы колич. лет пользования продуктами банка, колич. используемых банк. продуктов по странам'''
#sns.barplot(x="Geography", y="Tenure", hue="NumOfProducts", data=data, palette='hls')


'''Визуализация 3D диаграммы рассеивания'''
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
#x = data['NumOfProducts']
#y = data['Tenure']
#z = data['Age']
#
#ax.set_xlabel("NumOfProducts")
#ax.set_ylabel("Tenure")
#ax.set_zlabel("Age")
#
#ax.scatter(x, y, z)

plt.show()
