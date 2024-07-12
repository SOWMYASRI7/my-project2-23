def partition(a, l, r):
    pivot = a[r]
    gindex = l
    for k in range(l, r):
        if a[k] <= pivot:
            if gindex != k:
                a[k], a[gindex] = a[gindex], a[k]
            gindex += 1
    a[gindex], a[r] = a[r], a[gindex]
    return gindex

def q(a, l, r):
    if l >= r:
        return
    pivot = partition(a, l, r)
    q(a, l, pivot - 1)
    q(a, pivot + 1, r)

a = [12, 4, 32, 16, 23]
q(a, 0, len(a) - 1)
print(a)
