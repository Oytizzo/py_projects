def selection_sort(L):
    n = len(L)

    for i in range(0, n-1):
        index_of_min = i

        for j in range(i+1, n):
            if L[j] < L[index_of_min]:
                index_of_min = j
            
        if index_of_min != i:
            L[i], L[index_of_min] = L[index_of_min], L[i]


if __name__ == "__main__":
    L = [3, 6, 1, 2, 5]
    print("Before sort: ", L)
    selection_sort(L)
    print("After sort: ", L)
