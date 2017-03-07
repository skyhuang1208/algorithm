import random
import quicksort
import statistics
from time import perf_counter as timer

#*** test how fast the implemented quicksort is  ***#

def check_quicksort(seq):
    for i, v in enumerate(seq[:-1]):
        if v > seq[i+1]:
            exit("incorrect: %d %f %f" % (i, v, seq[i+1]))

t1= []
t2= []
for i in range(40):
    x= int(2**(i/2))
    print("\r", i, x, end='')
    
    t= []
    for j in range(10):
        seq= [ random.random() for j in range(x) ]
        start= timer()
        quicksort.quicksort(seq)
        end= timer()
        check_quicksort(seq)
        t.append(end-start)
    t1.append( (statistics.mean(t), statistics.stdev(t)) )
    
    t= []
    for j in range(10):
        seq= [ random.random() for j in range(x) ]
        start= timer()
        seq.sort()
        end= timer()
        t.append(end-start)
    t2.append( (statistics.mean(t), statistics.stdev(t)) )

OFILE= open("time_quicksort.txt", "w")
for i in range(40):
    x= int(2**(i/2))
    print(i, x, t1[i][0], t1[i][1], t2[i][0], t2[i][1], file=OFILE)

