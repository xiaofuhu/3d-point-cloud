# Took reference from the post by Florent Poux, Ph.D. on Towards Data Science
# https://towardsdatascience.com/discover-3d-point-cloud-processing-with-python-6112d9ee38e7
# 
# Author: Fuhu Xiao

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np 
import os

DATA_DIR = "data"
F_NAME = "sample_w_normals.xyz"

if __name__ == "__main__":
    fig1 = plt.figure()
    fig2 = plt.figure()
    pc = np.loadtxt(os.path.join(DATA_DIR, F_NAME), skiprows=1, max_rows=10000)
    mean_z = np.mean(pc, axis=0)[2]
    spatial = pc[abs(pc[:, 2] - mean_z) < 1]
    xyz = spatial[:, :3]
    rgb = spatial[:, 3:6]
    abc = spatial[:, 6:]
    ax = fig1.gca(projection='3d')
    sc = fig2.gca(projection='3d')
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    a = abc[:, 0]
    b = abc[:, 1]
    c = abc[:, 2]
    ax.quiver(x, y, z, a, b, c, length=0.1, normalize=True)
    sc.scatter(x, y, z, c=rgb/255, s=0.1)
    plt.show()