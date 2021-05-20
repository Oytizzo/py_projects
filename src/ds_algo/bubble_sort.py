def buble_sort(L):
    n = len(L)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


if __name__ == "__main__":
    L = [4, 2, 1, 5, 3, 8, 7, 6]
    print("Before sort: ", L)
    buble_sort(L)
    print("After sort: ", L)
