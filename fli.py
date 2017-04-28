import getpass
import os
import shutil
import argparse

THRESHOLD = 400000
EXTENSION = '.jpg'
COUNTER = 0

parser = argparse.ArgumentParser(description='Windows 10 Login Image Finder Script')
parser.add_argument('-t', '--threshold', help = 'Minimum size for conversion, in bytes (default: 400KB)')
parser.add_argument('-e', '--extension', help = 'Extension to give to the found files')
parser.add_argument('-c', action = 'store_true', help = 'Clears the fli folder before executing')
args = vars(parser.parse_args())

#are the args not None?
if (args['extension'] not in [None, '.jpg', '.png', '.jpeg', '.gif', '.bpg']):
    print ('Extension not supported. Consider running with -h')
    exit()
elif (args['extension'] != None):
    EXTENSION = args['extension']

if (args['threshold'] != None):
    THRESHOLD = args['threshold']

if (args['c']):
    if (os.path.isdir('fli')):
        os.chdir('fli')
        for i in os.listdir():
            os.remove(i)
        os.chdir('..')

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
