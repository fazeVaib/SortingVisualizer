# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import plotly.graph_objects as go
from sortings import bubbleSort, insertionSort, quickSort, mergeSort, selectionSort, heapSort
from generateData import generateData

#%% [markdown]
# ### Define number of elements needed

#%%
num = 80


#%%
y, colors = generateData(num)
data = [go.Bar(
            y= y,
            marker_color = colors
    )]
layout = {'yaxis': {'showgrid':False,
                    'showticklabels': False,
                   'zeroline' : False,
                   'fixedrange':True},
         'xaxis' : {'showgrid' : False,
                   'zeroline':False,
                   'showticklabels':False,
                    'fixedrange':True,
                   'title':'Number of operations: 0'},
         'plot_bgcolor':'rgba(0,0,0,0)'}
fig = go.FigureWidget(data, layout)
# fig.show(config={'displayModeBar':False})
fig


#%%
bar = fig.data[0]
lay = fig.layout
# print(fig.data[0].y)


#%%
# bubbleSort.sort(bar, lay, num, colors)
# insertionSort.sort(bar, lay, num, colors)
# quickSort.sort(bar, lay, num, colors)
# mergeSort.sort(bar, lay, num, colors)
# selectionSort.sort(bar, lay, num, colors)
heapSort.sort(bar, lay, num, colors)


