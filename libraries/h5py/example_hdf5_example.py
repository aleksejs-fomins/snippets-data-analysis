import h5py
import numpy as np

h5f = h5py.File("mytestfile.hdf5", "w")

data = np.array([[1,2], [2,3], [3,4]])
dset = h5f.create_dataset("ground_graphs", data.shape, data=data, dtype='i')
grp = h5f.create_group("subgroup")
grp["aaa"] = 123


h5f.close()

# h5f = h5py.File('mytestfile.hdf5','r')
# print(h5f['ground_graphs'][:])
# h5f.close()

