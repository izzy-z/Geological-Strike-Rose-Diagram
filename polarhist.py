import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("/Users/isabellaz/Desktop/HappyHollow/Untitled spreadsheet - Sheet1.csv")
data['centers'] = (data['min'] + data['max']) / 2

centers = data['centers'].to_numpy()
bar_height = data['count'].to_numpy()
centers = np.deg2rad(centers)
WIDTH = 10

plt.style.use('ggplot')
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1, projection='polar')
COLOR = ['powderblue', 'lightsalmon', 'navajowhite']
ax.bar(centers, bar_height, width=np.deg2rad(WIDTH), bottom=0.0, color=COLOR, edgecolor='slategrey')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
plt.title("Happy Hollow Pebble Orientations")

plt.show()