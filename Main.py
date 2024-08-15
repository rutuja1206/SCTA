import pandas as pd
import numpy as np


data = pd.read_csv("Screentime - App Details.csv")
print(data.head())

#Checking for null values
data.isnull().sum()

#Descriptive Statistics of Data
print('Descriptive Statistics')

#Analyzing amount of usage of the apps:
figure = pd.bar(data_frame=data,
                x = "Data",
                y = "Usage",
                color = "App",
                title = "Usage")
figure.show()

#No. of Notifications from the apps
figure = pd.bar(data_frame=data,
                x = "Date",
                y = "Notifications",
                color = "App",
                title = "Notifications")
figure.show()

#No. of times the apps opened
figure = pd.bar(data_frame=data,
                x = "Date",
                y = "Time opened",
                color = "App",
                title = "Time Opened")
figure.show()
