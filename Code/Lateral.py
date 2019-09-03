import numpy as np
import cv2
import os

base = '../Pictures/Worked/'
images = os.listdir(base)

output 	= cv2.imread(base + images[0])
image1 	= cv2.imread(base + images[1])

cv2.addWeighted(image1, 1.0/len(images) , output, 1.0/len(images), 0, output)
output1 = output
cv2.addWeighted(image1, 1.0/2, output1, 1.0/2, 0, output1)
cv2.imwrite("Lateral/" + str(101) + ".png", output1)
for i in range(2, len(images)):
	print(i)
	image1 = cv2.imread(base + images[i])
	cv2.addWeighted(image1, 1.0/len(images), output, 1, 0, output)
	cv2.addWeighted(image1, 1.0/(i+1), output1, 1.0*i/(i+1), 0, output1)

	cv2.imwrite("Lateral/" + str(100 + i) + ".png", output1)