import os
from dotenv import load_dotenv

load_dotenv()   # loads values from .env file

db_pass = os.getenv("DB_PASSWORD")

print(db_pass)