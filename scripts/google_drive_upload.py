from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

class AssetPublisher():
    # def authenticate(self):
    #     self.gauth = GoogleAuth()

    #     self.gauth.LocalWebserverAuth()

    #     self.drive = GoogleDrive(self.gauth)

    def authenticate(self):
        credentials_path = "credentials/"

        self.gauth = GoogleAuth()

        self.gauth.LoadCredentialsFile(os.path.join(credentials_path, "credentials.txt"))

        if self.gauth.credentials is None:
            # self.gauth.LocalWebserverAuth(client_config_file=client_secrets)
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()

        try:
            self.gauth.SaveCredentialsFile(os.path.join(credentials_path, "credentials.txt"))
        except:
            os.mkdir("credentials")
            self.gauth.SaveCredentialsFile(os.path.join(credentials_path, "credentials.txt"))

        self.drive = GoogleDrive(self.gauth)

    def upload_asset(self, file, folder_id):
        name = file.rsplit(".", 1)[0]

        path = f"hip/geo/{file}"

        file = self.drive.CreateFile({"title": name, "parents": [{"id": folder_id}]})
        file.SetContentFile(path)
        file.Upload()
        print(f"Asset < {name} > was successfully uploaded.")


if __name__ == "__main__":
    gdp = AssetPublisher()
    gdp.authenticate()

    folder_id = "1PQMTh0E4UeufWK8TJNsDTqMnXZd5-9Xj"

    files = os.listdir("hip/geo")
    for file in files:
        gdp.upload_asset(file, folder_id)

