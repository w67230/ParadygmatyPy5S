import string
from functools import reduce
import numpy



def laczMacierze(lista : list, funkcja : string):
    return reduce(eval(funkcja), lista);



A = numpy.array(
    [
        [2],
        [3],
        [5]
    ]
);

B = numpy.array(
    [
        [1, 4, 8]
    ]
);

C = numpy.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
);

listaMacierzy = [A, B, C];

print(laczMacierze(listaMacierzy, "lambda x, y: x + y"));


