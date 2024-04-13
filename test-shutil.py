import shutil

#print(dir(shutil))

#copy file from path to anther
shutil.copy('req.txt','f:/')

#move file from path to anther
shutil.move('req.txt','f:/')

#copy alll folder from 1 to 2 
shutil.copytree('foldername path 1','foldername path 2')


