import os

def selfDestruct():
 #this PERMANENTLY deletes the running file
 path = os.path.abspath(__file__)
 os.system("del " + path)
