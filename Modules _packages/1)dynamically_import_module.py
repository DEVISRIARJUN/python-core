# 1. Write a Python program that attempts to dynamically import a module at runtime. The program should only import the module if it actually exists; otherwise, it should print "Module does not exist".



import importlib.util
import importlib
mod_name = input("Enter module name : ")

if importlib.util.find_spec(mod_name):
    module = importlib.import_module(mod_name)
    print("Imported the module sucessfully")
else:
    print("Module doesnot exists")


