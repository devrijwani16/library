# book CRUD API

A simple book CRUD Application built using FastAPI. This project demonstrates CRUD (Create, Read, Update, Delete) operations using local in-memory storage without any database.

---

## Features

✅ Create book

✅ Get All books

✅ Get book By ID

✅ Update book

✅ Delete book

---

## Project Structure

```text
book_curd/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── bookModel.py
│
├── controllers/
│   └── bookController.py
│
└── routers/
    └── bookRouter.py
```

---

## Requirements

Install required packages:

```bash
pip install fastapi uvicorn pydantic
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open terminal inside project folder and run:

```bash
uvicorn main:app --reload
```

If successful:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Swagger API Documentation

Open your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically where all APIs can be tested.

---

## API Endpoints

| Method | Endpoint |
|----------|----------|
| POST | `/books/postbooks` |
| GET | `/books/getbooks` |
| GET | `/books/getbook/{bookid}` |
| PUT | `/books/updatebook/{bookid}` |
| DELETE | `/books/deletebook/{bookid}` |

---

## How book CRUD Works

### Create book

Creates a new book and automatically assigns a unique ID.

Example:

```json
{
  "name": "Dev",
  "book_name": "be the men",
  "author": "dev",
  "publication": "dev",
  "year": 2009
}
```

### Get All books

Returns all book records stored in memory.

### Get book By ID

Returns a specific book using book ID.

Example:

```text
/books/getbook/1
```

### Update book

Updates the information of an existing book.

### Delete book

Deletes a book record using the book ID.

### Storage

This project stores data temporarily using:

```python
books = []
```

No database is used.

Data will be lost when the server stops.

---

## Git Cleanup

Before pushing to GitHub, remove Python cache files:

### Remove All __pycache__ Folders (Windows PowerShell)

```powershell
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

### Create .gitignore

```text
__pycache__/
*.pyc
venv/
.env
```

This prevents unnecessary files from being uploaded to GitHub.

---

## Git Commands Used

### Initialize Repository

```bash
git init
```

### Add Project Files

```bash
git add .
```

### Create Commit

```bash
git commit -m "Initial book CRUD Project"
```

### Create Main Branch

```bash
git branch -M main
```

### Connect GitHub Repository

```bash
git remote add origin <repository-url>
```

### Push Project to GitHub

```bash
git push -u origin main
```

### Check Repository Status

```bash
git status
```

### View Commit History

```bash
git log --oneline
```

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

---

## Author

**Dev Rijwani**

MSc IT book