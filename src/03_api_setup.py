import os


serper_api_key = os.getenv("SERPER_API_KEY")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY environment variable is not set.")

os.environ["SERPER_API_KEY"] = serper_api_key
