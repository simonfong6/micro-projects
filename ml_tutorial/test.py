import svm as SVM
import numpy as np

data_dict = {	-1:np.array(	[[10,9,1],
				[2,8,1],
				[3,8,1],]),
             
		1:np.array(	[[5,1,1],
        	                 [6,-1,1],
        	                 [7,3,1],])}

svm = SVM.Support_Vector_Machine()
svm.fit(data=data_dict)

predict_us = [[0,10,1],
	      [1,3,1],
	      [3,4,1],
	      [3,5,1],
	      [5,5,1],
	      [5,6,1],
	      [6,-5,1],
	      [5,8,1]]

for p in predict_us:
	svm.predict(p)
svm.visualize()

