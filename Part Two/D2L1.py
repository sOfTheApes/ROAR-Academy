import numpy as np

v = np.array([2.,2.,4.])

e0 = np.array([1.,0.,0.])
e1 = np.array([0.,1.,0.])
e2 = np.array([0.,0.,1.])

E0 = np.dot(v,e0)
E1 = np.dot(v,e1)
E2 = np.dot(v,e2)

print(E0, E1, E2)
