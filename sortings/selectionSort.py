import time


def sort(bar, layout, num, colors):
    '''
    bar : first attribute of figure data which consists of dictionary that stores all information of plot
    layout : layout parameter of the figure
    num : number of elements to sort
    colors : color array the consists of color info of all elements to sort 
    '''

    data = list(bar.y)
    count = 0

    for i in range(num): 
        min_index = i
        for j in range(i+1, num): 

            count += 1
            layout.xaxis.title.text = "Number of operations: " + str(count)

            if data[min_index] > data[j]:
                colors[j] = 'crimson'
                colors[min_index] = 'lightslategray'
                colors[i] = 'red'
                bar.marker.color = colors
                time.sleep(0.1)
                min_index = j
            else: 
                colors[j] = 'green'
                bar.marker.color = colors
                time.sleep(0.1)

            colors[j] = 'lightslategray'
            colors[min_index] = 'red'
            bar.marker.color = colors
    
        data[min_index], data[i] = data[i], data[min_index]
        count += 1
        layout.xaxis.title.text = "Number of operations: " + str(count)
        colors[min_index] = 'lightslategray'
        bar.y = data
        colors[i] = 'blue'
        bar.marker.color = colors
