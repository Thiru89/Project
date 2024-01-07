from azure.cosmos import CosmosClient, exceptions, PartitionKey
import os, json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

#load the keys from the env file
url = os.environ.get("cosmosdb_url")
key = os.environ.get("cosmosdb_credentials")

client = CosmosClient(url, credential=key)

# list databases
database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)

# list container
container_name = 'products'

try:
    container = database.create_container(id = container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
    raise

# Load data into the container
for i in range(1, 10):
    container.upsert_item({
            'id': 'item{0}'.format(i),
            'productName': 'Widget',
            'productModel': 'Model {0}'.format(i)
        }
    )

# Enumerate the returned items
for item in container.query_items(
        query='SELECT * FROM mycontainer r WHERE r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))