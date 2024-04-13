import os



path='F:/bola'
os.chdir(path)

for file in os.listdir():
    file_name , file_extensin = os.path.splitext(file)
    file_title , file_number = file_name.split(' ')
    new_name =f'{file_number}-{file_title}-{file_extensin}'
    os.rename(file,new_name) 


