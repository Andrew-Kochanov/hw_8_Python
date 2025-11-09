def bubble_sort(list):
    lenght = len(list)
    for i in range(lenght):
        for j in range(i + 1, lenght):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list