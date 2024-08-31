import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("files/Churn_Modelling.csv")
#plt.style.use('classic')


'''Одну и ту же информацию "Количество клиентов по странам" отражаем двумя графиками на одной плоскости'''
#plt.title('Number Of Clients', fontsize='16')
#plt.plot(data['Geography'].value_counts(), 'r--o', markerfacecolor='orange', markersize=10)
#plt.bar(x=data['Geography'].value_counts().index, # Возвращает индекс (Страны)
#        height=data.Geography.value_counts().values, width=0.5) # Возвращает "Количество клиентов каждой страны"
#plt.xlabel('Countries', fontsize='14') # Подписываем ось 'x'
#plt.ylabel('Customers', fontsize='14') # Подписываем ось 'y'


'''Круговые графики с помощью метода (pie)'''
#fig, ax = plt.subplots()
#explode=[0.02, 0.05, 0.08]
#ax.pie(data.Geography.value_counts(), labels=data.Geography.value_counts().index, explode=explode,
#       shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'} )
#plt.title('Geography', fontsize=16)
#samp = data.sample(n=10)
#fig1, (ax1, ax2) = plt.subplots(1, 2)
#plt.suptitle('Круговые графики (pie)', fontsize=16)
#ax1.pie(samp['Age'], labels=samp['Age'], autopct='%1.1f%%')
#ax1.set_title('Age')
#ax2.pie(data.Gender.value_counts(), labels=data.Gender.value_counts(), explode=[0.02, 0.03], autopct='%1.1f%%')
#ax2.set_title('Gender')
#ax.axis('equal')
#ax1.axis('equal')
#ax2.axis('equal')



'''Гистограмма Баланса'''
plt.hist(x=data['Balance'], bins=20, histtype='stepfilled', rwidth=0.7, color='orange',
         edgecolor='black', label='Balance')
plt.legend()
plt.title('Histogram of Balance')
plt.xlabel('Balance')
plt.ylabel('Row number')


'''Двухмерное распределение признаков'''
#samp = data.sample(n=100)
#plt.scatter(x=samp['Balance'], y=samp['Age'],marker='*',s=80, c='red', edgecolor='grey',
#            linewidth=1) # Рассматриваем баланс относительно возраста клиента, с методом 'scatter'
#plt.bar(x=samp['Geography'], height=samp["Balance"], width=0.5) # Балан относительно странам с методом 'bar'


'''Создание двух графиков в рамках одной сетки'''
#fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
#gender = data.Gender.value_counts()
#products = data.NumOfProducts.value_counts()
#ax1.bar(x=gender.index, height=gender.values)
#ax2.bar(x=products.index, height=products.values)

'''Групировка пола по возрасту с помощью Boxplot'''
#ax = data.boxplot(column='Age', by='Gender', color='r')
#ax.set_ylabel('Age')


plt.grid()
plt.show()


