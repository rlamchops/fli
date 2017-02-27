import getpass
import os
import shutil

THRESHOLD = 400000
EXTENSION = '.jpg'
COUNTER = 0

#first get the current user
currentUser = getpass.getuser()

#now put it in position
formatString = 'C:\\Users\\{}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
fullPath = formatString.format(currentUser)

#create a folder in the current directory to hold the images
os.makedirs('fli', exist_ok = True)
storagePath = os.path.realpath('fli')

#change to the directory where the images are
os.chdir(fullPath)

#check files one at a time
for name in os.listdir('.'):
    #if one passes, copy it into the previously made directory
    if (os.stat(name).st_size > THRESHOLD):
        shutil.copy(name, storagePath)
        print ("Found " + name + " : " + str(os.stat(name).st_size) + " bytes")

os.chdir(storagePath)

#the copied files have no extensions. need to add the specified one
for name in os.listdir('.'):
    os.replace(name, name + EXTENSION)
    COUNTER += 1

print ('Done. Made ' + str(COUNTER) + ' images. They can be found in ' + storagePath + '.')
