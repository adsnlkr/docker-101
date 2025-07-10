# 🚀 Basic Dockerized FastAPI App

A minimal FastAPI application in Python 3.9 featuring:

- Health check endpoint
- Auto-generated Swagger UI
- Docker support for easy deployment


## ✅ Prerequisites

Make sure you have the following installed:

- **Python 3.9**  
  - Verify: `python3.9 --version`  
  - [Install Python](https://www.python.org/downloads/)

- **pip** (Python package manager)  
  - Usually included with Python  
  - Verify: `pip --version`

- **Virtual Environment**  
  - Included with Python 3.9+  
  - Example creation:
    ```bash
    python3.9 -m venv venv
    ```

- **Docker** *(optional, for container deployment)*  
  - Verify: `docker --version`  
  - [Install Docker](https://docs.docker.com/get-docker/)



## ✨ Features

- `/health` endpoint for health checks
- Interactive Swagger UI at `/docs`
- Redoc documentation at `/redoc`
- Dockerized for easy container deployment
- Compatible with Python 3.9



## 📁 Project Structure

...


## ⚡ Quick Start
1️⃣ Clone the repository
``` bash
git clone repo-link
cd app-folder
```
2️⃣ Create and activate virtual environment

macOS / Linux
```
python3.9 -m venv venv
source venv/bin/activate
```

Windows (PowerShell)
```
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install dependencies
```
pip install -r requirements.txt
```

4️⃣ Run the application
```
uvicorn app.main:app --reload
```

✅ Access in your browser:
* Health check: http://127.0.0.1:8000/health
* Swagger docs: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc