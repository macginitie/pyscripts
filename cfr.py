import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sys

csvfile = sys.argv[1]
df = pd.read_csv(csvfile)

# dx = list(map(lambda x:x/10, df[' worldwide deaths per Wikipedia']))

#fig = go.Figure(data=[
#    go.Bar(name='U.S.', x=df['date'], y=df[' U.S. deaths per Wikipedia']),
#    go.Bar(name='World/10', x=df['date'], y=dx)
#])

fig = make_subplots(
    rows=1, cols=2,
    shared_xaxes=False,
    vertical_spacing=0.03,
    specs=[[{"type": "bar"},
            {"type": "bar"}]]
)

fig.add_trace(
    go.Bar(name='U.S.', x=df['date'], y=df[' U.S. deaths per Wikipedia']),
    row=1, col=1
)

fig.add_trace(
    go.Bar(name='World', x=df['date'], y=df[' worldwide deaths per Wikipedia']),
    row=1, col=2
)

fig.update_layout(
    height=800,
    showlegend=True,
    title_text="COVID-19 cumulative death counts according to Wikipedia",
)

fig.show()
