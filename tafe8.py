# import the PyFilesystem library for OS files
# from time import clock_settime
# import errno
# from lib2to3.pgen2.token import STRING
# from tokenize import String
# from xmlrpc.client import Boolean
from distutils.log import error
from fs.osfs import OSFS
import os

# from fs.zipfs import ZipFS


#  open a local filesystem for the current directory

def creat_dir(dirname, path):
    with OSFS(".\TMP") as myfs:
        if (not myfs.exists(dirname)):
            #create a  data directory
            myfs.makedir(dirname)
            print('dir %s created' % dirname)
        else: 
            print('dir %s exists' % dirname)
    error = False
    return error
    
def read_file (filename):
    # with myfs.open("testdir/samplefile.txt", mode='w') as f:
      # read the file contents
    #   content = f.read()
      content = open(filename, "r")
      print ('-' * 45)
      print('Clients Database:')
      print(content.read())
      print ('-' * 45)
    #   content = open(filename, "r")
      with open(filename) as x:
        lines = x.readlines()
      x.close()
      error= False
      return (lines, error)

def ask_file ():
    print ('-' * 45)
    # filename = input("Please input file name to read:")
    filename = 'clients'
    if not(os.path.exists(filename)): 
       print('error')
       error=True
    else: 
        print("using [%s] file" %(filename))
        error=False
    return (filename, error)



def ask_folders_path ():
    print ('-' * 45)
    #folders = input("Please input path where to create customer folders:")
    folders = "TMP"
    if not(os.path.exists(folders)) or not(os.path.isdir(folders)):
       print('error: folder doesnot exists')
       error = True
    else: 
        print("using [%s] PATH" %(folders))
        error = False
    return (folders, error)



def main():
    os.system("cls")
    filename, error = ask_file()
    if error==False: 
        folderspath, error = ask_folders_path()
    if error==False: 
        ClientDataLines, error = read_file(filename)
        print('Creating Clients Directories')
        for x in ClientDataLines:
            x = x.replace("\n", "")
            creat_dir(x, folderspath)       

    

    
            
    

if __name__== "__main__":
   main()







