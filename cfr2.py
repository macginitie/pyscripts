import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sys

csvfile = sys.argv[1]
df = pd.read_csv(csvfile)

def diff(data, index):
    if index < 2:
        return 0
    print(index)
    try:
        return int(data[index]) - int(data[index - 1])
    except:
        print('!', data[index])
        return 0
        
def smooth(data):
    for idx in range(len(data)- 1):
        if data[idx] == 0:
            # 2DO: make this work for multi-day skips too
            data[idx] = data[idx+1]/2
            data[idx+1] /= 2

diff_world = []
wrld_data = df[' worldwide deaths per Wikipedia']
for idx in range(len(wrld_data)):
    diff_world.append(diff(wrld_data, idx))

smooth(diff_world)

diff_US = []
us_data = df[' U.S. deaths per Wikipedia']
for idx in range(len(us_data)):
    diff_US.append(diff(us_data, idx))
    
smooth(diff_US)    

fig = make_subplots(
    rows=1, cols=2,
    shared_xaxes=False,
    vertical_spacing=0.03,
    specs=[[{"type": "bar"},
            {"type": "bar"}]]
)

fig.add_trace(
    go.Bar(name='U.S.', x=df['date'], y=diff_US),
    row=1, col=1
)

fig.add_trace(
    go.Bar(name='World', x=df['date'], y=diff_world),
    row=1, col=2
)

fig.update_layout(
    height=800,
    showlegend=True,
    title_text="COVID-19 daily death counts according to Wikipedia",
)

fig.show()
