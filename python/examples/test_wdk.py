from numpy import mat, repmat, transpose, zeros, ones
from numpy import array,concatenate,arange,double

from shogun.Features import *
from shogun.Kernel import *

# create toy data

degree=20;
seqlen=60;

ex1 = array(seqlen*['A'])
ex2 = array(seqlen*['C'])
ex3 = []
ex3 += 'ACTGAAGAAGATCTGAATAAATTTGAGTCTCTTACCATGGGGGCAAAGAAGAAGCTCAAG'
XT = transpose([ex1,ex2,ex3])

trainfeat = CharFeatures(XT,DNA)

wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree)
K = mat(wdk.get_kernel_matrix())
print K

weights = arange(1,degree+1,dtype=double)[::-1]/sum(arange(1,degree+1,dtype=double))
wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, weights=weights)
K = mat(wdk.get_kernel_matrix())
print K

wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, block_computation=False, use_normalization=False)
K = mat(wdk.get_kernel_matrix())
print K

weights = arange(1,degree+1,dtype=double)[::-1]/sum(arange(1,degree+1,dtype=double))
wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, block_computation=False, use_normalization=False, weights=weights)
K = mat(wdk.get_kernel_matrix())
print K

weights = arange(1,degree+1,dtype=double)[::-1]/sum(arange(1,degree+1,dtype=double))
wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, block_computation=True, use_normalization=False, weights=weights)
K = mat(wdk.get_kernel_matrix())
print K

weights = arange(1,degree+1,dtype=double)
wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, block_computation=False, use_normalization=False, weights=weights)
K = mat(wdk.get_kernel_matrix())
print K

weights = arange(1,degree+1,dtype=double)
wdk = WeightedDegreeCharKernel(trainfeat, trainfeat, degree, block_computation=True, use_normalization=False, weights=weights)
K = mat(wdk.get_kernel_matrix())
print K

