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

    for i in range(1, num):

        key = data[i]
        j = i-1

        count += 1
        layout.xaxis.title.text = "Number of operations: " + str(count)

        while j>=0 and key < data[j]:

            data[j+1] = data[j]
            colors[j+1] = 'blue'
            colors[j] = 'yellow'
            bar.marker.color = colors
            bar.y = data
            time.sleep(0.1)

            colors[j] = 'blue'
            bar.marker.color = colors
            j -= 1

            count += 1
            layout.xaxis.title.text = "Number of operations: " + str(count)

        data[j+1] = key
        bar.y = data
        colors[i] = 'blue'
        bar.marker.color = colors
