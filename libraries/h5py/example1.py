import h5py
import numpy as np

f = h5py.File("mytestfile.hdf5", "w")
# dset = f.create_dataset("mydataset", (100,), dtype='float')

aaa = (
    np.linspace(0,1,100),
    np.linspace(0,1,100)
)

f['mydataset'] = aaa
f.close()

# print(dset)