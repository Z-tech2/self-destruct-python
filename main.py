#this PERMANENTLY deletes the running python file when used
def selfDestruct():
 from os import path,system
 path = os.path.abspath(__file__)
 os.system("del " + path)
