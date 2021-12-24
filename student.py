import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv(
    r"D:\Coding\python codes\data-analysis-by-visualisation\analysation\data.csv")

student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
    x=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    y=student_df.groupby("level")["attempt"].mean(),
    orientation='v'))

fig.show()
