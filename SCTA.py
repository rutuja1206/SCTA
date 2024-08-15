import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime - App Details.csv")
print(data.head())

#Checking if the data set has any null values
data.isnull().sum()

#Descriptive statics of data
print(data.describe())

#The amount of usage of the apps
figure = px.bar(data_frame=data,
                x = "Date",
                y = "Usage",
                color = "App",
                title = "Usage")
figure.show()

#The Number of Notification from the apps
figure = px.bar(data_frame=data,
                 x = "Date",
                 y = "Notificatios",
                 color = "App",
                 title = "Notifications")
figure.show()

#The Number of times apps opened
figure = px.bar(data_frame = data,
                x = "Date",
                y = "Times opened",
                color = "App",
                title = "Times Opened")
figure.show()

#Relationship between the no. of notification and amount of usage

figure = px.scatter(data_frame = data,
                    x="Notifications",
                    y="Usage",
                    size="Notifications",
                    trendline="ols",
                    title="Relationship between no. of notification and usage")
figure.show()
