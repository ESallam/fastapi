from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from PIL import Image
import requests

import APIVault
from Item import Item

app = FastAPI()

@app.post("/OCR_EG_NationalID_Front")
def OCR_EG_NationalID_Front(SecurityKey: str, ImageUrl: str):
    if SecurityKey == APIVault.GetSecurityKey():
        im = Image.open(requests.get(ImageUrl, stream=True).raw)
        return im.size
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error Loading Image")
