import os

from google.colab import userdata

serper_api_key = userdata.get("serper_api_key")
os.environ["SERPER_API_KEY"] = serper_api_key
