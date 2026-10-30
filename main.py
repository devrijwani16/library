# pip install fastapi uvicorn pydantic
# uvicorn main:app --reload

#Remove-Item -Recurse -Force __pycache__

#git init then # git add .
# git remote -v
# git remote set-url origin https://github.com/devrijwani16/library.git  
# git push -u origin main

# "Renamed main.py to book_crud.py" //  uvicorn book_crud:app --reload

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import bookRouter
from routers.bookRouter import bookRouter

app = FastAPI()
app.include_router(bookRouter)

# render try to run on https://book-curd.onrender.com 
@app.get("/")
def home():
    return RedirectResponse(url="/docs")

