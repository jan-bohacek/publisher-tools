import hou
import sys
import importlib 

path = r"C:\Users\janbo\Documents\Projekty\practice\houdini\td\publisher-tools\scripts"
status = ""

if path not in sys.path:
    sys.path.append(path)
    import publisher_hda
    status = "module LOADED"
else:
    import publisher_hda
    importlib.reload(publisher_hda)
    status = "module RE-LOADED"
    
# for i in sys.path:
#     print(i)
print(status)
