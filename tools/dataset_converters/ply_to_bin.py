import numpy as np
import pandas as pd
import os
from plyfile import PlyData

newbac = '.bin'

def convert_ply(input_path, output_path):
    plydata = PlyData.read(input_path)  # read file
    data = plydata.elements[0].data  # read data
    data_pd = pd.DataFrame(data)  # convert to DataFrame
    data_np = np.zeros(data_pd.shape, dtype=np.float64)  # initialize array to store data
    property_names = data[0].dtype.names  # read names of properties
    for i, name in enumerate(
            property_names):  # read data by property
        data_np[:, i] = data_pd[name]
    data_np.astype(np.float32).tofile(output_path)

plyfile = os.listdir('./pointclouds')
for v in plyfile:
    ply_address = './pointclouds'
    plyfiles = os.path.join(ply_address,v)
    # print(plyfiles)
    bin_address = './bin'
    #binfiles输出的是./bin/xxxx.ply，所以还需要通过下面的rename将输出的,ply转换为.bin
    binfiles = os.path.join(bin_address,v)
    # print(binfiles)

    #rename(ply-bin)
    fname, bac = os.path.splitext(binfiles)
    base_name = os.path.basename(fname)
    new_name = os.path.join(bin_address, base_name + newbac)
    # print(new_name)

    convert_ply(plyfiles,new_name)








#convert_ply('./pointclouds/003392.ply', './bin/003392.bin')
