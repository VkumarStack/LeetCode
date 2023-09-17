def SignificantInversions(ordering):
    if len(ordering) == 1:
        return 0
    
    m = len(ordering) // 2
    l = ordering[:m]
    r = ordering[m:]
    A = SignificantInversions(l)
    B = SignificantInversions(r)
    # Count Inversions Before Merging
    C = CountSignificantInversions(l, r)
    
    # Merge
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ordering[k] = l[i]
            i = i + 1
        else:
            ordering[k] = r[j]
            j = j + 1
        k = k + 1
    while i < len(l):
        ordering[k] = l[i]
        i = i + 1
        k = k + 1
    while j < len(r):
        ordering[k] = r[j]
        j = j + 1
        k = k + 1

    return A + B + C

def CountSignificantInversions(A, B):
    inversions = 0
    i = len(A) - 1
    j = len(B) - 1
    while i != -1 and j != -1:
        if A[i] > 2 * B[j]:
            inversions += j + 1
            i = i - 1
        else:
            j = j - 1
    return inversions