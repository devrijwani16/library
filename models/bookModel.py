# from urllib import 
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class book(BaseModel):
    id: Optional[int] = None
    book_name: str
    author: str
    publication: str
    year: int