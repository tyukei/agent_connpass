import os
from dotenv import load_dotenv
load_dotenv()

CONNPASS_API_KEY = os.getenv("CONNPASS_API_KEY")

# connpassのイベントを作成する.APIは、READしかできないので、Playwrightを使用して、connpassのイベントを作成する.
def create_event():
    