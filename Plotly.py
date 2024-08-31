import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


data = pd.read_csv("files/Churn_Modelling.csv")
print(data.head(5))


'''Диаграмма рассеяния который показывает кред.рейтинг относительно фамилий клиентов выбранных нами рандомно'''
samp = data.sample(n=5)
#fig = px.scatter(samp, x='Surname', y='CreditScore', color='Age', size='CreditScore')

'''Фасеточное построение, графики, разделенные по значению атрибута, отображаются в виде таблицы.'''
#fig = px.scatter(data, x='Balance', y='Age', facet_col='Gender', color='Geography')
#facet_col разбивает график на количество частей по указанному параметру

'''Определяем количество используемых банк. продуктов по каждому полу с помощью столбчатой диаграммы'''
#fig = px.bar(data, x='Gender', y='NumOfProducts', color='Gender',template='ggplot2')
#fig.update_layout({'plot_bgcolor': 'white',   # цвет фона графика белый
#                   'paper_bgcolor': 'grey'})  # цвет общего фона серый

'''Гистограмма по возрасту'''
#fig = px.histogram(data, x='Age', color='Age', title='Histogram of Age')
#fig.update_layout(title={'font': dict(size=35), 'x':0.5}, yaxis_title='Count')

'''Круговые графики с помощью метода (pie)'''
#fig = px.pie(samp, values='Surname', names='CreditScore', title='Круговой график')


#fig = px.area(samp, x="Surname", y="Balance", color="Age", line_group="Age")

'''Воронкообразная диаграмма'''
#fig = px.funnel(samp, x='Age', y='Surname', color='Balance')
#fig = go.Figure(go.Funnelarea(text = data.Geography.value_counts().index,
#                              values = data.Geography.value_counts().values))

fig.show()


