import numpy as np


masks_points = []
mask0_points = []
mask0_labels = []

#positive points
mask0_points.append([1250,805])
mask0_labels.append(1)

mask0_points.append([1250,700])
mask0_labels.append(1)

mask0_points.append([590,780])
mask0_labels.append(1)

mask0_points.append([590,650])
mask0_labels.append(1)

mask0_points.append([1100,150])
mask0_labels.append(1)

mask0_points.append([700,1020])
mask0_labels.append(1)

mask0_points.append([1350,300])
mask0_labels.append(1)

mask0_points.append([1500,400])
mask0_labels.append(1)


#negative points
#mask0_points.append([1250,800]) 
#mask0_labels.append(0)

masks_points.append([np.array(mask0_points, dtype=np.float32), np.array(mask0_labels, np.int32)])
