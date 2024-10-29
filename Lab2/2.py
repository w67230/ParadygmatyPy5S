import numpy
import string


def wykonajOperacje(operacja : string):
    return eval(operacja);




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

print(wykonajOperacje("A*B"));


