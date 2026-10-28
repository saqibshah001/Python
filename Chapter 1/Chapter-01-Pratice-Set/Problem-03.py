# is problem mai ham ny Chat gpt sy eysa program banwana hai jis sy mere folder ky under kya hai ye pata chaly

# Beginners level function

import os

directory_path = r'C:\Users\Shah\Documents\Python'

contents = os.listdir(directory_path)

for item in contents:
    print(item)



# Advance level function3

# import os

# directory_path = r'C:\Users\Shah\Documents\Python'

# for root, directories, files in os.walk(directory_path):
#     print("\nCurrent Folder:", root)

#     for directory in directories:
#         print("Folder:", directory)

#     for file in files:
#         print("File:", file)
