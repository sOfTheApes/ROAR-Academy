from matplotlib import image
from matplotlib import pyplot
import os

lenna = image.imread("../samples/lenna.bmp").copy()
flag = image.imread("usa.jpg")

for w in range(len(flag[0])):
	for h in range(len(flag)):
		lenna[h][-w] = flag[h][-w]

pyplot.imshow(lenna)
pyplot.show()
