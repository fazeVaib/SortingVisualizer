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
    alldata = list(bar.y)
    msort(data, bar, layout, num, colors, 0, alldata)


def msort(data, bar, layout, num, colors, startindex, alldata): 
    global count
    if len(data)>1: 
        mid = len(data)//2
        rightindex = startindex + mid
        left = data[:mid]
        right = data[mid:]

        msort(left, bar, layout, num, colors, startindex, alldata)
        msort(right, bar, layout, num, colors, rightindex, alldata)

        i = j = k2 = 0
        k = startindex

        colors[startindex:rightindex] = ['yellow']* (rightindex - startindex)
        colors[rightindex:rightindex+mid] = ['orange'] * (mid)
        bar.marker.color = colors
        time.sleep(0.1)
        while i<len(left) and j<len(right):
            count += 1
            layout.xaxis.title.text = "Number of operations: " + str(count)
            if left[i] < right[j]: 
                alldata[k] = left[i]
                data[k2] = left[i]
                bar.y = alldata
                time.sleep(0.1)
                i += 1
            else:
                alldata[k] = right[j]
                data[k2] = right[j]
                bar.y = alldata
                time.sleep(0.1)
                j += 1
            k += 1
            k2 += 1

        while i < len(left): 
            count += 1
            layout.xaxis.title.text = "Number of operations: " + str(count)
            alldata[k] = left[i]
            data[k2] = left[i]
            bar.y = alldata
            time.sleep(0.1)
            i += 1
            k += 1
            k2 += 1

        while j < len(right): 
            count += 1
            layout.xaxis.title.text = "Number of operations: " + str(count)
            alldata[k] = right[j]
            data[k2] = right[j]
            bar.y = alldata
            time.sleep(0.1)
            j += 1
            k += 1
            k2 += 1

        bar.y = alldata
        time.sleep(0.1)
        colors[startindex:rightindex] = ['blue'] * (rightindex - startindex)
        colors[rightindex:rightindex+mid] = ['blue'] * (mid)
        bar.marker.color = colors
        time.sleep(0.1)
        # print(alldata)
