import os
from pymongo import MongoClient
import boto3

# password = os.environ.get("MONGODB_PWD")
# session = boto3.Session(profile_name='main')

client = boto3.client('ssm', region_name='us-east-1')

password = client.get_parameter(
    Name='/api/mongo/password',
    WithDecryption=True
)

pwd = password["Parameter"]["Value"]
print(pwd)
connection_string = f"mongodb+srv://ksalka:{pwd}@cluster0.wby46ms.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(connection_string)
