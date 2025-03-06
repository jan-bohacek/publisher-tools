import hou
import os

class AssetPublisher():
    def __init__(self):
        self.node = hou.pwd()

    def publish_asset(self):
        dir = self.node.parm("directory").eval()
        if dir.endswith("/"):
            dir = dir[:-1]
        asset = self.node.parm("asset_name").eval()
        
        try:
            files = os.listdir(dir)
            files = [x for x in files if x.endswith(".obj") and x.split("/")[-1].split(".")[0] == asset]
            version = f"v{len(files)+1:03}"
        except:
            version = "v001"
            
        print(asset)
        print(version)

        path = f"{dir}/{asset}.{version}.obj"
        
        path = self.node.parm("export_path").set(path)

        self.node.node("OUT_cache").parm("execute").pressButton()
        print(f"Asset <{asset}> was published successfully!")

        gdrive_name = f"{asset}.{version}"
        # google_drive_upload.upload_asset(gdrive_name, path)
        
    def load_asset(self):
        dir = self.node.parm("directory").eval()
        if dir.endswith("/"):
            dir = dir[:-1]
        asset = self.node.parm("asset").evalAsString()
        version = self.node.parm("version").evalAsString()
        
        path = f"{dir}/{asset}.{version}.obj"
        
        self.node.parm("import_path").set(path)
        
        file_node = self.node.parent().createNode("file", f"assetLoad_{asset}")
        file_node.parm("file").set(path)
        file_node.setColor(hou.Color(0.5,0.8,0.2))
        file_node.moveToGoodPosition()
        
        print(f"Asset <{asset}> was loaded successfully!")
        
        