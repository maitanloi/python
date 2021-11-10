import os
def main(): # Function to rename multiple files
   i = 1
   path="/Volumes/Dev/Python/rename/file-hinh/"
   for filename in os.listdir(path):
      my_dest ="gui-hang-di-my-" + "100" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      os.rename(my_source, my_dest)
      i += 1
if __name__ == '__main__':
   main() # Calling main() function