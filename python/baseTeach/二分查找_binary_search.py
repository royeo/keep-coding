# 二分查找
data = list(range(1, 50, 3))
print(data)


def binary_search(src, find_n):
    mid = int(len(src) / 2)

    if len(src) >= 1:
        if src[mid] > find_n:
            binary_search(src[:mid], find_n)
        elif src[mid] < find_n:
            binary_search(src[mid:], find_n)
        else:
            print('find number: [%s]' % find_n)
    else:
        print("can't find")


binary_search(data, 1)
