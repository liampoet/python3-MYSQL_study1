def insertion_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        key = li[i]
        while li[j] > key and j >= 0:
            li[j+1] = li[j]
            j = j -1
        li[j+1] = key
    return li

if __name__ == "__main__":
	li = [4, 6, 1, 7, 2, 8, 3, 5, 9, 10, 12, 11]
	insertion_sort(li)