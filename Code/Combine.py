import numpy as np
import cv2
import os

# base = 'Pictures/Worked/'
# images = os.listdir(base)
# for k in range(0,len(images),110):
# 	print(k)
# 	end 	= min(k + 110, len(images))
# 	output 	= cv2.imread(base + images[k + 0])
# 	image1 	= cv2.imread(base + images[k + 1])

# 	cv2.addWeighted(image1, 1.0/(end - k) , output, 1.0/(end - k), 0, output)

# 	for i in range(2,end - k):
# 		print(images[k + i])
# 		# load the image
# 		image1 = cv2.imread(base + images[k + i])
# 		cv2.addWeighted(image1, 1.0/(end - k), output, 1, 0, output)
# 	print(k)
# 	cv2.imwrite("Pictures/Combined/Output" + str(k) + ".png", output)

base = 'Pictures/Positions/'
base2 = 'Pictures/Worked/'
folders = os.listdir(base)

for folder in folders:
	if(folder  + '.png' not in os.listdir("Pictures/Positions_combined/")):
		images = os.listdir(base + folder)
		output 	= cv2.imread(base2 + images[0])
		image1 	= cv2.imread(base2 + images[1])

		cv2.addWeighted(image1, 1.0/len(images) , output, 1.0/len(images), 0, output)
		print(folder)
		for i in range(2, len(images)):
			image1 = cv2.imread(base2 + images[i])
			cv2.addWeighted(image1, 1.0/len(images), output, 1, 0, output)

		cv2.imwrite("Pictures/Positions_combined/" + folder + '.png', output)