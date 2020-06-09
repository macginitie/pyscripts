import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sys

csvfile = sys.argv[1]
df = pd.read_csv(csvfile)

# hacks to deal with missing values
last_recorded = 0

def diff(data, index):
    global last_recorded
    if index < 2:
        return 0
    subtrahend = 0
    minuend = 0
    try:
        subtrahend = int(data[index - 1])
        last_recorded = subtrahend
    except:
        print('! @{0}=>{1} - {2}'.format(index, data[index], data[index - 1]))
    try:
        minuend = int(data[index])
        last_recorded = minuend
    except:
        print('! @{0}=>{1} - {2}'.format(index, data[index], data[index - 1]))

    if minuend < subtrahend or minuend == 0:
        return 0
    if subtrahend == 0:
        return minuend - last_recorded
    return minuend - subtrahend
        
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
