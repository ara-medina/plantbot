import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost/{os.getenv('POSTGRES_DB')}"
db = SQLAlchemy(app)

@app.route('/')
def hello():
    try:
        db.session.execute(text('SELECT 1'))
        return "Hello from AI Garden Planner Backend! Database connection successful."
    except Exception as e:
        return f"Hello from AI Garden Planner Backend! Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)