import os, time
import scipy.io as spio

# Print root level values of dict (result of loadmat)
def inspect_mfile(d):
    for k,v in d.items():
        if isinstance(v, float) or isinstance(v, int) or isinstance(v, list):
            print(k, v)
        else:
            print(k, v.shape)

# Convert "scipy.io.matlab.mio5_params.mat_struct object" to dict
def matstruct2dict(matstruct):
    return {s : [getattr(matstruct, s)] for s in dir(matstruct) if s[0]!='_'}

def loadmat(filename, waitRetry=None):
    '''
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    '''
    
    # Test if file is accessible, and retry indefinitely if required
    fileAccessible = os.path.isfile(filename)
    if not fileAccessible:
        if waitRetry is None:
            raise ValueError("Matlab file can not be accessed", filename)
        else:
            while not fileAccessible:
                print("... can't reach file, waiting", waitRetry, "seconds")
                time.sleep(waitRetry)
                fileAccessible = os.path.isfile(filename)

    # Load data
    data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    
    # Get rid of useless keys
    data = {k : v for k, v in data.items() if k[0] != '_'}
    
    return _check_keys(data)

def _check_keys(d):
    '''
    checks if entries in dictionary are mat-objects. If yes
    todict is called to change them to nested dictionaries
    '''
    for key in d:
        if isinstance(d[key], spio.matlab.mio5_params.mat_struct):
            d[key] = _todict(d[key])
    return d        

def _todict(matobj):
    '''
    A recursive function which constructs from matobjects nested dictionaries
    '''
    d = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, spio.matlab.mio5_params.mat_struct):
            d[strg] = _todict(elem)
        else:
            d[strg] = elem
    return dict


# # Recursively convert "scipy.io.matlab.mio5_params.mat_struct" objects to dicts
# def _check_keys(d):
#     for k,v in d.items():
#         print(k, type(v))
#         if isinstance(v, spio.matlab.mio5_params.mat_struct):
#             v_tmp = {s : [getattr(v, s)] for s in dir(v) if s[0]!='_'}
#             d[k] = _check_keys(v_tmp)
#         elif isinstance(v, dict):
#             d[k] = _check_keys(v)
#     return d