"""Load the Serper API key and expose it through the environment."""

import os


SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY environment variable is not set.")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY
