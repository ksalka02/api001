import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

# find dotenv file automatically (goes through files until it finds it)
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)


password = os.getenv("MONGODB_PWD")

connection_string = f"mongodb+srv://ksalka:{password}@cluster0.wby46ms.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
