from fastapi import FastAPI
from pydantic import BaseModel
import pyodbc
# Create a web API using FastAPI with a route to products.
app = FastAPI()

class products(BaseModel):
    name: str
    description: str
    price: float

@app.get("/products")
async def get_products(products: BaseModel):
    # Logic to fetch and return products
    #return {"message": "Get all products"}
    return products

@app.post("/products")
async def create_product():
    # Logic to create a new product
    return {"message": "Create a new product"}

@app.put("/products/{product_id}")
def update_product(product_id: int):
    # Logic to update a product
    return {"message": f"Update product with ID: {product_id}"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    # Logic to delete a product
    return {"message": f"Delete product with ID: {product_id}"}

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    # Execute SQL query to fetch a single product by ID
    cursor.execute(f"SELECT * FROM Products WHERE ProductID = {product_id}")
    product = cursor.fetchone()

    if product:
        # Return the product details
        return {"message": f"Get product with ID: {product_id}", "product": product}
    else:
        # Return a message if product is not found
        return {"message": f"Product with ID: {product_id} not found"}

