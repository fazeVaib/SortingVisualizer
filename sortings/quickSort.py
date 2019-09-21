import time

count = 0

def sort(bar, layout, num, colors):
    '''
    bar : first attribute of figure data which consists of dictionary that stores all information of plot
    layout : layout parameter of the figure
    num : number of elements to sort
    colors : color array the consists of color info of all elements to sort 
    '''

    data = list(bar.y)
    quicksort(data, 0, num-1, bar, layout, colors)
    colors = ['blue',] * num
    bar.marker.color = colors


def quicksort(data, low, high, bar, layout, colors):
    if low < high: 
        pi = partition(data, low, high, bar, layout, colors)
        quicksort(data, low, pi-1, bar, layout, colors)
        quicksort(data, pi+1, high, bar, layout, colors)


def partition(data, low, high, bar, layout, colors):
    i = low - 1
    global count 
    pivot = data[high]
    colors[high] = 'yellow'
    bar.marker.color = colors

    for j in range(low, high):
        count += 1
        layout.xaxis.title.text = "Number of operations: " + str(count)

        if data[j] <= pivot: 
            i += 1
            data[i], data[j] = data[j], data[i]
            colors[i] = 'green'
            colors[j] = 'green'
            bar.marker.color = colors
            bar.y = data
            time.sleep(0.1)
            colors[i] = 'lightslategray'
            colors[j] = 'lightslategray'
            bar.marker.color = colors
        else:
            colors[i] = 'crimson'
            colors[j] = 'crimson'
            bar.marker.color = colors
            time.sleep(0.1)
            colors[i] = 'lightslategray'
            colors[j] = 'lightslategray'
            bar.marker.color = colors

    colors[high] = 'lightslategray'
    colors[i] = 'red'
    colors[j] = 'red'
    bar.marker.color = colors
    data[i+1], data[high] = data[high], data[i+1]
    count += 1
    layout.xaxis.title.text = "Number of operations: " + str(count)
    bar.y = data
    time.sleep(0.1)
    colors[i] = 'lightslategray'
    colors[j] = 'lightslategray'    
    bar.marker.color = colors
    return i+1
