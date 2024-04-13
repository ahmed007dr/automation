import os

#dir name = folders
#file name = files.txt

# for dirpath , dirname , filenames in os.walk('.'):
#     if not dirname and not filenames:
#         os.rmdir(dirpath)

#loop in hard desk

for dirpath , dirname , filenames in os.walk('c:'):
    print(dirpath)