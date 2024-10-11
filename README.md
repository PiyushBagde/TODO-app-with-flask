# TODO App with Flask 🗒️

A simple and efficient TODO app built with Flask, allowing users to create, update, and delete tasks. This app uses a minimalistic design for task management and stores data locally in a SQL database.

## Features

- **Create Tasks:** Add new tasks with a description and due date.
- **Update Tasks:** Edit task details and mark tasks as complete.
- **Delete Tasks:** Remove tasks when no longer needed.
- **Task List:** View a list of all tasks with their current status (pending or completed).
- **Responsive Design:** User-friendly interface that works on various devices.
___
## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS (Bootstrap for styling)

___
To run this project locally, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/PiyushBagde/TODO-app-with-flask.git
cd TODO-app-with-flask
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 4. Initialize the Database
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```
### 5. Run the Flask Application
```bash
flask run
```
