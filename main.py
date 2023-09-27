import fractions
import numpy as np
A_inv = np.array([ 0.62087912, -0.42307692,  0.24725275])
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
print(A_inv)