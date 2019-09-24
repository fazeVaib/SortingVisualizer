import time

count = 0
def heapify(arr, n, i, bar, colors, layout):
    # Find largest among root and children
    global count
    count += 1
    layout.xaxis.title.text = "Number of operations: " + str(count)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        colors[largest] = 'lightslategray'
        colors[l] = 'yellow'
        bar.marker.color = colors
        time.sleep(0.1)
        largest = l

    if r < n and arr[largest] < arr[r]:
        colors[largest] = 'lightslategray'
        largest = r
        colors[r] = 'yellow'
        bar.marker.color = colors
        time.sleep(0.1)

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        colors[largest] = 'red'
        colors[i] = 'red'
        bar.marker.color = colors
        time.sleep(0.1)
        arr[i], arr[largest] = arr[largest], arr[i]
        bar.y = arr
        colors[largest] = 'lightslategray'
        colors[i] = 'lightslategray'
        bar.marker.color = colors
        time.sleep(0.1)
        heapify(arr, n, largest, bar, colors, layout)


def sort(bar, layout, num, colors):
    '''
    bar : first attribute of figure data which consists of dictionary that stores all information of plot
    layout : layout parameter of the figure
    num : number of elements to sort
    colors : color array the consists of color info of all elements to sort 
    '''

    data = list(bar.y)
    global count
    # Build max heap
    for i in range(num, -1, -1):
        count += 1
        layout.xaxis.title.text = "Number of operations: " + str(count)
        heapify(data, num, i, bar, colors, layout)
        bar.y = data

    for i in range(num-1, 0, -1):
        # swap
        count += 1
        layout.xaxis.title.text = "Number of operations: " + str(count)
        colors[i] = 'green'
        colors[0] = 'green'
        bar.marker.color = colors
        time.sleep(0.1)
        data[i], data[0] = data[0], data[i]
        bar.y = data
        colors[i] = 'blue'
        colors[0] = 'lightslategray'
        bar.marker.color = colors

        #heapify root element
        heapify(data, i, 0, bar, colors, layout)
        bar.y = data
    
    colors[0] = 'blue'
    bar.marker.color = colors
    count = 0
    # print(data)
