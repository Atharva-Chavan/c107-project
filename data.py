import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv(r"D:\Coding\python codes\data-analysis-by-visualisation\analysation\data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=['Level 1', 'Level 2', 'Level 3', 'Level 4'], 
    y=df.groupby("level")["attempt"].mean(), 
    orientation='v')) 
    
fig.show()
