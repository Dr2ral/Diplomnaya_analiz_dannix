import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd


data = pd.read_csv("files/Churn_Modelling.csv")

fig = px.scatter(data, x='Geography', y='Balance')
fig.show()


