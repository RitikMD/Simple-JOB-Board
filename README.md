# Simple-JOB-Board
# Simple Job Board API

A minimal RESTful API for managing job postings.

## Features

- CRUD operations for job postings
- Organized by routes, models, schemas, and database files

## Project Structure

```
Simple_Job_Board_API/
├── api/         # API routes
├── app/         # Main application and database setup
├── crud/        # CRUD operations
├── models/      # Data models
├── schemas/     # Data validation schemas
├── requirements.txt
```

## Setup

1. **Create and activate a virtual environment (recommended):**

   On Linux/macOS:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Navigate to the project folder:**
   ```
   cd Simple_Job_Board_API
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```
   python app/init_db.py
   ```

5. **Start the application:**
   ```
   uvicorn app.main:app --reload
   ```

## License

MIT
