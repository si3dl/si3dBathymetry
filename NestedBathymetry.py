# -------------------------------------------------------------------------
# This codes serves to create the file needed as bathymetry for the SI3D
# model when doing NESTED BOUNDARY CONDITIONS.
#
# Version 1: This version includes the designation of points to be the
# boundaries for the nested simulations. It is only developed for real
# bathymetry cases.
#
# USAGE OF CODE
#
# Author: Sergio Valbuena
# Date: 04-29-2020
#
# -------------------------------------------------------------------------
# Library Import
import sys
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sci
import datetime as Dt
import pytz
import pandas as pd
import time
import pickle
import math

# Declaration of mathematical constants
pi = math.pi
Omega = 7.2921e-5   #[rad/s] Rotation rate of earth
g = 9.801           #[m/s2] Gravitational accelaration

# Definition of variables
Sim_Name = 'Lake Tahoe   R44'
dx_save = '(dx=  25m),'
Path_Bathy = 'G:/My Drive/Lake_Tahoe/Projects/Upwelling_3DModel/Bathymetry'
Path_save = 'G:/My Drive/Lake_Tahoe/Projects/Upwelling_3DModel/Bathymetry/si3D'
PathLocation = 'G:/My Drive/Lake_Tahoe/Projects/Upwelling_3DModel/Validation_Data'
os.chdir(Path_Bathy)
mindepth = -0.2
cdx = 100
fdx = 25
# Options for cut direction:
# NS WE NSE SNE NSW SNW NSENW
CutDir = 'NS'

# Verification of length of header in SI3D File
Entry = Sim_Name+dx_save
if len(Entry) != 27:
    error(['Please add/remove spaces before dx_save to complete 27 characteres. The current number of characteres is: ',str(len(Entry))])
else:
    print('Number of characteres in Lake Name and dx is good to save in the h file for SI3D')

# Loading bathymetry file 
F_Bathy_File = 'LakeTahoeGrid'+str(fdx)+'m'
