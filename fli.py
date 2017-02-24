import getpass
import os

THRESHOLD = 400000
EXTENSION = '.jpg'

#first get the current user
currentUser = getpass.getuser()

#now put it in position
formatString = 'C:\\Users\\{}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
fullPath = formatString.format(currentUser)

#create a folder in the current directory to hold the images


#change to the directory where the images are
os.chdir(fullPath)

#open files one at a time and perform the check
for name in os.listdir('.'):
    if (os.stat(name).st_size > THRESHOLD):
        print ("Found " name + EXTENSION + " : " + str(os.stat(name).st_size) + " bytes")
