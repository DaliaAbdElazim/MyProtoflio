## Project Setup Instructions

### 1. Clone the Project

To get a copy of this project, open your terminal and run the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL of the project repository.

### 2. Access the Project Directory

Navigate into the project directory by running:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the name of the cloned directory.

### 3. Install `virtualenv`

Before creating a virtual environment, ensure you have `virtualenv` installed. You can install it using pip:

```bash
pip install virtualenv
```

### 4. Create a Virtual Environment

Once `virtualenv` is installed, create a virtual environment by running:

```bash
virtualenv venv
```

### 5. Activate the Virtual Environment

Activate the virtual environment using the following command:

- **For Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **For macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 6. Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 7. Run the Development Server

After installing the dependencies, open a terminal (if not already open) and run the following commands:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=true
flask run --reload
```

The development server should now be running. You can access the application in your web browser at `http://127.0.0.1:5000`.

### Notes on Database Connection in `models.py`

1. **Local Database Connection:**
   - If you have added a password to your MySQL database while using **MySQL Workbench**, you can establish a connection using the following format:
     ```python
     database_path = "mysql+mysqlconnector://{}@{}/{}".format('root:', 'localhost', MYSQL_DB)
     ```
   - This setup is useful for local development where you have direct access to your MySQL server through MySQL Workbench.

2. **Cloud SQL Connection via TCP:**
   - For connecting to a Cloud SQL instance using TCP while working locally, you can use the following connection string:
     ```python
     database_path = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?unix_socket=/cloudsql/{PROJECT_ID}:{MYSQL_REGION}:{MYSQL_DB}"
     ```
   - This configuration is specifically designed for local testing of Cloud SQL connections.

3. **Production Connection with Unix Socket:**
   - When deploying to a production environment (e.g., App Engine or Cloud Run), you can connect to the database using a Unix socket:
     ```python
     database_path = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@/{MYSQL_DB}?unix_socket={MYSQL_UNIX_SOCKET}"
     ```
   - This method is only applicable when the application is running on Google Cloud services, providing a secure and efficient connection to the database.
