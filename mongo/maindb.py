# from dotenv import load_dotenv, find_dotenv
import os
# import pprint
from pymongo import MongoClient
# load_dotenv(find_dotenv())
import boto3

# password = os.environ.get("MONGODB_PWD")
client = boto3.client('ssm', region_name='us-east-1')

password = client.get_parameter(
    Name='/api/mongo/password',
    WithDecryption=True
)

connection_string = f"mongodb+srv://ksalka:{password}@cluster0.wby46ms.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
