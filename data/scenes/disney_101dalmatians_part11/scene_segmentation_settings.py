import numpy as np


masks_points = []
mask0_points = []
mask0_labels = []

#positive points
mask0_points.append([500,450])
mask0_labels.append(1)

mask0_points.append([800,500])
mask0_labels.append(1)

mask0_points.append([900,400])
mask0_labels.append(1)

#negative points
#mask0_points.append([1250,800]) 
#mask0_labels.append(0)

masks_points.append([np.array(mask0_points, dtype=np.float32), np.array(mask0_labels, np.int32)])
