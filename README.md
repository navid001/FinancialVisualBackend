# FinancialVisualBackend

A Flask backend API for visualizing financial data over 5 years, deployed on Render.

## Project Structure
```
FinancialVisualBackend/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── database.py
├── instance/
│   └── financial_data.db
├── .env
├── config.py
├── requirements.txt
├── init_db.py
├── run.py
└── gunicorn_config.py
```

## Local Development Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- virtualenv

### Installation Steps

1. Clone the repository:
```bash
git clone [https://github.com/navid001/FinancialVisualBackend.git]
cd FinancialVisualBackend
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

4. Copy env.example file:
```bash
cp .env.example .env
```
```env
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=sqlite:///instance/financial_data.db
SECRET_KEY=your-secret-key-here
```

5. Initialize the database:
```bash
python3 init_db.py
```

6. Run the application:
```bash
python3 run.py
```

Server will start at `http://localhost:5000`

## API Endpoints

- `GET /api/financial-data` - Returns all monthly financial data
- `GET /api/summary` - Returns yearly summaries
- `GET /api/trends` - Returns growth trends

## Deployment to Render

### Prerequisites for Render Deployment
1. Create a Render account at [render.com](https://render.com)
2. Push your code to a Git repository (GitHub/GitLab)

### Required Files for Render

1. Update `requirements.txt` with Gunicorn:
```
flask==2.3.3
flask-sqlalchemy==3.1.1
flask-cors==4.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

2. Create `gunicorn_config.py`:
```python
bind = "0.0.0.0:10000"
workers = 2
threads = 4
timeout = 120
```

3. Update `.gitignore`:
```
venv/
__pycache__/
instance/
.env
*.pyc
```

### Deployment Steps

1. Log in to Render Dashboard

2. Click "New +" and select "Web Service"

3. Connect your Git repository

4. Configure the Web Service:
   - Name: `FinancialVisualBackend` (or your preferred name)
   - Environment: `Python 3`
   - Build Command: `pip3 install -r requirements.txt`
   - Start Command: `./start.sh`
   - Plan: Free (or your preferred plan)

5. Add Environment Variables in Render Dashboard:
   ```
   FLASK_APP=run.py
   FLASK_ENV=production
   DATABASE_URL=sqlite:///instance/financial_data.db
   SECRET_KEY=your-production-secret-key
   ```

6. Click "Create Web Service"

