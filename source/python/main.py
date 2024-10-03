
## @py-check
## @py-requirement requests


from fastapi import FastAPI
from pydantic import BaseModel
import hashlib
import base64
import os

app = FastAPI()

class Text(BaseModel):
    """Text class inherits from BaseModel"""
    text = str()

@app.post("/checksum")
def calculate_checksum(text: Text):
    """Endpoint to calculate checksum of the text"""
    checksum = hashlib.md5(text.text.encode()).hexdigest()
    return {"checksum": checksum}

def main():
    # Define the text to calculate checksum for
    text = "Hello, world!"

    # Create a dictionary payload with the text
    payload = {"text": text}

    # Send a POST request to the /checksum endpoint
    response = requests.post("http://localhost:8000/checksum", json=payload)

    # Print the response
    print(response.json())

if __name__ == "__main__":
    main()