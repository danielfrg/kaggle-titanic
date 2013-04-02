import copper
import pandas as pd

copper.project.path = '../'

players = copper.read_csv('players.csv')

print(players)
print(players.groupby('team').groups)


