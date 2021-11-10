import os # import os module
path_name = r'/Volumes/Dev/Python/rename/file-hinh/' # folder path and destination
for count, filename in enumerate(os.listdir(path_name)): # loop through the directory to rename all the files
        new ="pic-" + "100" + str(count+1) + '.jpg'  # new file name
        src = os.path.join(path_name, filename)  # file source
        dst = os.path.join(path_name, new)  # file destination
        os.rename(src, dst) # rename all the file