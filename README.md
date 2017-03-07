## Algorithm implementations  ##

### quicksort.py module ###
It includes **quick sort** and **quick select** algorithm implementation.  
Pivot is randomly selected and then move to the end to avoid worst cases. 
The implemenation uses recusive calls

* def quicksort(seq)  
Sort the list "seq". Sorting is performed in-place, meaning seq will be modified to sorted sequence. No return values.

* def quickselect(seq, target)  
Return the i-th smallest value in the list "seq", which i is specified by target. Note that the target is counted  from 1, 2, ..., not from 0, 1, 2, ...
The input list seq will first be copied to a new one, meaning the original sequence is remained unchanged.

### Example codes and results ###
* ex_quicksort.py calculates the time complexity of my quicksory versus python inner sort metho.
* ex_quickselect.py tests my quickselect method
* quick_complexity.png shows the result of computing time as a function of data size

