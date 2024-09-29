from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from settings import MYSQL_UNIX_SOCKET, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_HOST, MYSQL_REGION, PROJECT_ID

# If you have added a password to your database, you need to add it here
# database_path = "mysql+mysqlconnector://{}@{}/{}".format('root:', 'localhost', MYSQL_DB)

# In case you want to use cloud SQL host and connect with TCP, use the following [Only working locally]
# database_path = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?unix_socket=/cloudsql/{PROJECT_ID}:{MYSQL_REGION}:{MYSQL_DB}"

## For using in production with Unix socket [Only Working with app engine/cloud run not locally with python app.py]
database_path = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@/{MYSQL_DB}?unix_socket={MYSQL_UNIX_SOCKET}"

db = SQLAlchemy()

def setup_db(app, database_path=database_path): 
    # For using in production 
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        'connect_args': {
            'connect_timeout': 28800,
        }
    }
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

        # Seed the database with a default portfolio if none exists
        seed_default_portfolio()

def seed_default_portfolio():
    # Check if any portfolio already exists
    existing_portfolio = Portfolio.query.first()

    if not existing_portfolio:
        # Create a new default portfolio
        default_portfolio = Portfolio(
            name='John Doe',  # Default name
            title='Software Developer',  # Default title
            bio='This is a default bio for the portfolio.',  # Default bio
            email='johndoe@example.com',  # Default email
            profile_picture_url='https://placehold.co/400',  # Default profile picture
            linkedin_link='',  # Default LinkedIn
            github_link='',  # Default GitHub
            cv_link=''  # Default CV link (can be empty)
        )

        # Insert default portfolio into the database
        try:
            default_portfolio.insert()
            print("Default portfolio seeded successfully.")
        except Exception as e:
            print(f"Error seeding default portfolio: {str(e)}")

class Portfolio(db.Model):
    """
    Database model for portfolio data.

    Attributes:
        id (int): Portfolio ID (primary key).
        name (str): Portfolio owner's name.
        title (str): Portfolio owner's title.
        bio (str): Short biography or description.
        email (str): Portfolio owner's email address.
        profile_picture_url (str): URL for the profile picture.
        linkedin_link (str): URL for the LinkedIn profile.
        github_link (str): URL for the GitHub profile.
        cv_link (str): URL for the CV or resume.
    """
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Name should not be empty
    title = db.Column(db.String(100), nullable=True)  # Title for the portfolio
    bio = db.Column(db.Text, nullable=True)  # Bio can be longer text, nullable in case it's not provided
    email = db.Column(db.String(100), nullable=True)  # New email field
    profile_picture_url = db.Column(db.String(300), nullable=True)  # URL for the profile picture
    linkedin_link = db.Column(db.String(300), nullable=True)  # URL for the LinkedIn profile
    github_link = db.Column(db.String(300), nullable=True)  # URL for the GitHub profile
    cv_link = db.Column(db.String(300), nullable=True)  # URL for the CV or resume

    def insert(self):
        """
        Insert a new portfolio entry into the database.

        Raises:
            SQLAlchemyError: If there's an error inserting the portfolio entry into the database.
        """
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error inserting portfolio: {str(e)}")
            raise

    def update(self):
        """
        Update the portfolio entry in the database.

        Raises:
            SQLAlchemyError: If there's an error updating the portfolio entry in the database.
        """
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating portfolio: {str(e)}")
            raise

    def delete(self):
        """
        Delete the portfolio entry from the database.

        Raises:
            SQLAlchemyError: If there's an error deleting the portfolio entry from the database.
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting portfolio: {str(e)}")
            raise

    def format(self):
        """
        Format portfolio object into a dictionary representation.

        Returns:
            dict: Dictionary representation of the portfolio object.
        """
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,  # Include title in the formatted output
            'bio': self.bio,
            'email': self.email,  # Include email in the formatted output
            'profile_picture_url': self.profile_picture_url,
            'linkedin_link': self.linkedin_link,
            'github_link': self.github_link,
            'cv_link': self.cv_link
        }
