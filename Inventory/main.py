from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)


redis = get_redis_connection(
    host="redis-19877.c256.us-east-1-2.ec2.cloud.redislabs.com",
    port="19877",
    password="NKCfY6skP39pQUi0NFlT8ifJb6mMWtXc",
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int
    
    class Meta:
        database = redis
    
@app.get('/products')
def all():
    return Product.all_pks()
@app.post('/products')
def create(product: Product):
    return product.save
