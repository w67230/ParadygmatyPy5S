import numpy
from numpy import transpose
import string


def wykonajOperacje(operacja : string):
    try:
        wynik = eval(operacja);
    except ValueError:
        print("Niepoprawna operacja");
        wynik = [];

    return wynik;




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

print(wykonajOperacje("transpose(A) * B"));


