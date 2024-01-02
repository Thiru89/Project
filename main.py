import numpy as np
import pandas as pd
import pinecone 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override = True)
print(os.environ.get("PINECONE_API_KEY"))

import pinecone

# Create an index
# "dimension" needs to be same as dimensions of the vectors you upsert
pinecone.create_index(index_name="products", dimension=1536)

# Connect to the index
index = pinecone.Index(index_name="products")

# Mock vector and metadata objects (you would bring your own)
vector = [0.010, 2.34,...] # len(vector) = 1536
metadata = {'text': "Approximate nearest neighbor search (ANNS) is a fundamental building block in information retrieval"}

# Upsert your vector(s)
index.upsert((id='some_id', values=vector, metadata=metadata)) # (id, vector, metadata)        