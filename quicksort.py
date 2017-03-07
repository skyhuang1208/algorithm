import random

# pivot is randomly selected for the methods below #
# ************************************************ #

### Using quicksort algorithm to sort an array
def quicksort(seq):
    qsort(seq, 0, len(seq)-1)

def qsort(seq, begin, end):
    if begin < end:
        ipvt= random.randint(begin, end)    # select random pivot
        seq[ipvt], seq[end]= seq[end], seq[ipvt]
        pivot= seq[end]

        left= begin                         # start sort
        for i in range(begin, end):
            if seq[i] <= pivot:
                seq[i], seq[left]= seq[left], seq[i]
                left +=1
        seq[left], seq[end]= seq[end], seq[left]

        qsort(seq, begin, left-1)           # sort left & right
        qsort(seq, left+1, end)


### Using quickselect algorithm to select the k-th smallest value
def quickselect(seq, target):
    if target>len(seq): exit("Error(quickselect): target lt len(seq) %d %d" % (target, len(seq)))
    return qselect(seq, 0, len(seq)-1, target)

def qselect(seq, begin, end, k):
    ipvt= random.randint(begin, end)    # select random pivot
    seq[ipvt], seq[end]= seq[end], seq[ipvt]
    pivot= seq[end]

    left= begin                         # searching
    for i in range(begin, end):
        if seq[i] <= pivot:
            seq[i], seq[left]= seq[left], seq[i]
            left +=1
    seq[left], seq[end]= seq[end], seq[left]

    if k==(left+1):  return seq[left]   # go deeper
    elif k<(left+1): return qselect(seq, begin, left-1, k)
    else:            return qselect(seq, left+1, end, k)

