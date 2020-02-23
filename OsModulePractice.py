import os
print(os.getcwd())
os.chdir("D:visualStudio\AFinalYearProject\AFinalYearProject\image")
print(os.getcwd())
print(os.listdir())
# os.makedirs('img_express')
# makes also subdirectories
# os.mkdir()
os.rmdir('img_express')