## FastAPI Async Architecture

### Description
 - Base FastAPI Project with asynchronization
 - This repository was written with inspiration from https://github.com/jujumilk3/fastapi-clean-architecture

### Base models
1. user
2. post [user (1:n) post]
3. tag [user (n:m) post]

### Run
```
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Test
```
ENV=test pytest --cov=app 
```
## ToDo
1. To apply migration tool such as alembic
