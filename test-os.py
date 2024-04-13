import os
from datetime import datetime

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
# print(os.stat('req.txt').st_size)

#from datetime import datetime
# print(datetime.fromtimestamp(os.path.getctime('req.txt')))


# for dirpath , dirnames , filenames in os.walk('.'):
#     print(dirpath)

# #dirpath           all path
# #dirname           all name
# #filename          all name

# #SEARCH UR HOME PAGEE IS OS
# print (os.environ.get('HOME'))


# #last file in path
# path = 'test/python/test.txt'
# print ('File last path :', os.path.basename(path))  
# #last folder with dirname
# print ('last file  :', os.path.dirname(path))      
# # split type file
# print ('File exists :', os.path.splitext(path))      
# #make sure path is true
# print ('File true :', os.path.exists(path))      

# print ('File folder not :', os.path.isfile(path))      
# print ('Folder True :', os.path.isdir(path))       

