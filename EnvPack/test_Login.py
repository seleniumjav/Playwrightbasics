import os

from dotenv import load_dotenv


def test_url():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    print(base_url)
    print("username:",os.getenv("USERNAME"))
    print("password:",os.getenv("PASSWORD"))

