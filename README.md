# plant-bot

An open-source garden planning tool that leverages AI to help users design, plan, and manage their gardens effectively.

## Project Status

This project is currently in early development. Features and documentation will be expanded over time.

## Features (Planned)

- Interactive garden layout planner
- Plant database with growing information
- AI-powered plant recommendations
- Planting calendar
- Climate-based advice

## Prerequisites

- Docker and Docker Compose
- Node.js and npm
- Python 3.8+
- PostgreSQL

## Setup and Installation

1. Clone the repository:
```
git clone https://github.com/ara-medina/plantbot.git
cd ai-garden-planner
```

2. Set up the backend:
```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the `backend` directory with your PostgreSQL credentials:
```
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=plantbot
```

4. Set up the frontend:
```
cd ..  # Make sure you're in the root directory
docker-compose up -d
```

## Running the Application

1. Start the backend:
```
cd backend
source venv/bin/activate  # On Windows use: venv\Scripts\activate
flask run
```

The backend will be available at `http://localhost:5000`.

2. In a new terminal, start the frontend:
```
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:5173` (or another port if 5173 is in use).

## Development

- Backend code is in the `backend` directory. The main file is `app.py`.
- Frontend code is in the `frontend` directory. 

## Contributing

We welcome contributions to this project. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) (to be created) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
