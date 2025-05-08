import numpy as np


masks_points = []
mask0_points = []
mask0_labels = []

#positive points
mask0_points.append([600,790])
mask0_labels.append(1)

mask0_points.append([900,500]) 
mask0_labels.append(1)

mask0_points.append([300,1000]) 
mask0_labels.append(1)

mask0_points.append([350,300]) 
mask0_labels.append(1)

mask0_points.append([430,560]) 
mask0_labels.append(1)

mask0_points.append([430,700]) 
mask0_labels.append(1)

mask0_points.append([1000,700]) 
mask0_labels.append(1)

mask0_points.append([430,740]) 
mask0_labels.append(1)

mask0_points.append([700,790]) 
mask0_labels.append(1)

mask0_points.append([750,1000]) 
mask0_labels.append(1)


mask0_points.append([250,700]) 
mask0_labels.append(0)

#negative points
#mask0_points.append([1250,800]) 
#mask0_labels.append(0)

masks_points.append([np.array(mask0_points, dtype=np.float32), np.array(mask0_labels, np.int32)])
