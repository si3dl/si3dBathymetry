# Bathymetry.py v1
# This code creates the bathymetry file of canonical lake basins and real lake basins for the si3d inputs.
# For the real lake bathymetry the user must define xg, yg, and zg before proceeding to run the code. xy,yg, and zg are 2-D matrices that contain the grid dimensions for the horizontal dimension based on a x=0,y=0 origin, and the vetical dimension (zg) uses the depth of the lake with origin z=0 at the lake's surface.
# Copy Right Sergio A. Valbuena 2021
# UC Davis - TERC
# February 2021

# Library Import
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as spio

# Import functions
root = "C://Users/"
user = "SV"
func = "/Documents/Github/si3dInputs/"
FuncPath = root + user + func
sys.path.append(FuncPath)
from si3dInputs import bathy4si3d
del root, user, func, FuncPath

# -------------------- User variables declaration -----------------------------
root = "S:/"
PathProject = "si3D/"
# Chose the name of folder for the simulation
SimFolder = 'L10_H100_W15_N10_f40'
# Chose path to save bathymetry file
PathSave = root+PathProject+SimFolder
# Chose the name of the simulation for the header in bathy files
# NOTE: This name requires an specific length. The length will be validated by the bathy4si3d code.
SimName = "Rect Basin R1   "
# Chose the grid size in the horizontal direction
dx = 500 #[m] in the x/y-horizontal direction
# Chose the basin type
# Use 1 for real lake Bathymetry
# Use 2 for rectangular basins
# Use 3 for spherical basins
# Use 4 for cylindrical basins
BasinType = 2
# Proper use and variables of func:
# if the basin is a real lake use the functions as: bathy4si3d(BasinType,SimName,dx,xg,yg,zg)
# if the basin is rectangular use the functions as: bathy4si3d(BasinType,SimName,dx,L,B,H)
# if the basin is spherical use the functions as: bathy4si3d(BasinType,SimName,dx,D,H)
# if the basin is cylindrical use the functions as: bathy4si3d(BasinType,SimName,dx,D,H)

if BasinType == 1:
    LakeName = 'LakeTahoeGrid'
    BathyPath = "G:/My Drive/Lake_Tahoe/Projects/Upwelling_3DModel/Bathymetry"
    # BathyPath = "G://My/Drive/Lake_Tahoe/Projects/Upwelling_3DModel/Bathymetry"
    BathyFile = LakeName + str(dx) + 'm.mat'
    mindepth = -0.2
    os.chdir(BathyPath)
elif BasinType == 2:
    L = 10000
    B = 10000
    H = 100
elif BasinType == 3:
    D = 10
    H = 10

 # -------------------- Beginning of Code to Create File -------------------------
# Function call for the creation of the bathymetry file in the folder PathSave
if BasinType == 1:
    [X,Y,Z] = bathy4si3d(BasinType,SimName,dx,PathSave,xg,yg,zg)
elif BasinType == 2:
    [X,Y,Z] = bathy4si3d(BasinType,SimName,dx,PathSave,L,B,H)
elif BasinType == 3:
    [X,Y,Z] = bathy4si3d(BasinType,SimName,dx,PathSave,D,H)
elif BasinType == 4:
    [X,Y,Z] = bathy4si3d(BasinType,SimName,dx,PathSave,D,H)
elif BasinType == 5:
    [X,Y,Z] = bathy4si3d(BasinType,SimName,dx,PathSave,D,H)


# ---------------- Plotting of the resulting bathymetric file ----------------------
fig,ax = plt.subplots()
fig.Units = 'inches'
plot = ax.pcolor(X,Y,np.flipud(Z))
fig.colorbar(plot)
ax.set_aspect('equal')
ax.grid(True, which='major',axis='both',linestyle='-',color=[0/255, 0/255, 0/255])
plt.draw()
plt.show()
