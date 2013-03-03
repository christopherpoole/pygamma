import numpy
import pylab

from dta import gamma_evaluation 

# Reference data with (2, 1) mm resolution
reference = numpy.random.random((128, 256))
#reference = numpy.abs(reference)
reference /= reference.max()
reference *= 100
reference -= 50

# Sample data with a %3 shift on the reference
sample = reference * 1.03

# Perform gamma evaluation at 4mm, 2%
gamma_map = gamma_evaluation(sample, reference, 4., 2., (2, 1), signed=True)

pylab.imshow(gamma_map, cmap='RdBu_r', aspect=2, vmin=-2, vmax=2)
pylab.colorbar()
pylab.show()

