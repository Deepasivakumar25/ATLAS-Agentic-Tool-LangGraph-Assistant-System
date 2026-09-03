import os
from importlib import import_module

serper_api_key = import_module("src.06_serper_api_key").serper_api_key
os.environ["SERPER_API_KEY"] = serper_api_key
