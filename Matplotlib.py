import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("files/Churn_Modelling.csv")
plt.style.use('classic')

'''Одну и ту же информацию "Количество клиентов по странам" отражаем двумя графиками на одной плоскости'''
#plt.title('Number Of Clients', fontsize='16')
#plt.plot(data['Geography'].value_counts(), 'r--o', markerfacecolor='orange', markersize=10)
#plt.bar(x=data['Geography'].value_counts().index, # Возвращает индекс (Страны)
#        height=data.Geography.value_counts().values, width=0.5) # Возвращает "Количество клиентов каждой страны"
#plt.xlabel('Countries', fontsize='14') # Подписываем ось 'x'
#plt.ylabel('Customers', fontsize='14') # Подписываем ось 'y'

'''Гистограмма Кредитного рейтинга'''
#plt.hist(x=data['CreditScore'], bins=20, range=(300, 900))


'''Двухмерное распределение признаков'''
#samp = data.sample(n=50)
#plt.scatter(x=samp['Balance'], y=samp['Age'], c='red' ) # Рассматриваем баланс относительно возраста клиента
#plt.bar(x=samp['Geography'], height=samp["Balance"], width=0.2)


'''Создание двух графиков в рамках одной сетки'''
#fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
#gender = data.Gender.value_counts()
#products = data.NumOfProducts.value_counts()
#ax1.bar(x=gender.index, height=gender.values)
#ax2.bar(x=products.index, height=products.values)

plt.grid()
plt.show()


