# import required libraries
import numpy as np


# defining the function used to iterate on a given input, using the recursive
# function given in the assignment handout
def iterate(re: float, im: float) -> tuple[int, int]:
    c = re + 1j*im  # computing complex input c from real and imaginary parts
    z0 = 0.  # setting z0 as given in handout
    zi = z0 + c  # defining the complex number to be used during iterations

    num_iterations = 0
    for _ in range(50):  # 50 iterations is arbitrarily chosen
        zi = zi**2 + c  # recursive step
        num_iterations += 1
        if abs(zi) > 10000:  # prevent excess computation if zi likely diverges
            break

    diverges = (abs(zi) >= 3*abs(c))  # if input diverges w.r.t. c with lenience

    return 0 + diverges, diverges * num_iterations  # if diverges, ~which iter.
