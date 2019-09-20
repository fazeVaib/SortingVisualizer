import time

def sort(bar, num, colors):

    '''
    bar : first attribute of figure data which consists of dictionary that stores all information of plot
    num : number of elements to sort
    colors : color array the consists of color info of all elements to sort 
    '''

    data = list(bar.y)

    for i in range(num):
        for j in range(num-i-1):

            if data[j] > data[j+1]:
                colors[j] = 'crimson'
                colors[j+1] = 'crimson'

                time.sleep(0.1)
                bar.marker.color = colors
                data[j], data[j+1] = data[j+1], data[j]
                bar.y = data

            else:
                colors[j] = 'green'
                colors[j+1] = 'green'
                time.sleep(0.1)
                bar.marker.color = colors

            colors[j] = 'lightslategray'
            colors[j+1] = 'lightslategray'
            bar.marker.color = colors

        colors[num-i-1] = 'blue'
        bar.marker.color = colors
