import os


path =  os.path.dirname(os.path.realpath(__file__))
inputpath = path+'/test-folder-in/'
outputpath = path+'/test-folder-out/'

print("Copying structure from")
print("  ", inputpath)
print("to")
print("  ", outputpath)

for dirpath, dirnames, filenames in os.walk(inputpath):
    # Get current relative path
    relpath = dirpath[len(inputpath):]
    print("Attempting to make a directory", relpath)

    # Make a new folder
    newfolderoutpath = os.path.join(outputpath, relpath)
    if not os.path.isdir(newfolderoutpath):
        os.mkdir(newfolderoutpath)
    else:
        print("-->Folder does already exits!")

    # List all filenames in that folder
    print("-->found files", filenames)