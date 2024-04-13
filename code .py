import os

# to print dir list for libary
#print(dir(os))

# The current path to the file
#print(os.getcwd())

#list in curreny dir
#print(os.listdir()) 

#change currenty dir
# print(os.getcwd())
# os.chdir('C:') # change it to your directory

#create empty file
#os.mkdir('test')

#create folder with path
#os.makedirs('python/basics')


#remove dir 
#os.rmdir('test')   # remove single folder

#remove mult folder
#os.removedirs('python')    # remove multi folders


# rename folder
#os.rename("old_name", "new_name")



#state folder
print(os.stat('req.txt').st_size)

from datetime import datetime
print(datetime.fromtimestamp(os.path.getctime('req.txt')))





