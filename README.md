# GoNow Sales AI Agent

This project is the backend service for the GoNow Sales AI Agent, built with [FastAPI](https://fastapi.tiangolo.com/). It is designed to cleanly integrate with your various data sources and AI models to automate and scale sales operations.

## Features

- **FastAPI Framework**: Modern, fast (high-performance), web framework for building APIs.
- **Pydantic Driven**: Environment and data validation via Python type annotations.
- **Cleaner Architecture**: Segregated application logic into modules (`api`, `core`).

## Project Structure

```bash
gonow_sale_agent/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py      # API Endpoint definitions
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py      # Pydantic environment configuration
│   ├── __init__.py
│   └── main.py            # Application execution root
│
├── .env                   # Environment Variables 
├── .gitignore             # Source control ignored items list
├── requirements.txt       # Python dependencies
└── README.md              # Project Documentation
```

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed locally.

## Installation & Setup

1. **Create the virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Update your `.env` file with the necessary credentials to change behavior across environments. A `.env` template looks like this:
   ```env
   PROJECT_NAME="GoNow Sales AI Agent"
   API_PREFIX="/api/v1"
   DEBUG=True
   ```

## Running the Application

To run the application locally for development with auto-reloading enabled, use Uvicorn:

```bash
uvicorn app.main:app --reload
```

Then visit your API interactively:
- **Health Check / Base Endpoint /:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Swagger UI Details:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Redoc Details:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Development

- Always remember to add any new pip dependencies directly to `requirements.txt` to keep environments synchronized.