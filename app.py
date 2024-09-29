from flask import Flask, request, render_template, redirect, url_for, flash
from flask_cors import CORS
from flask_ckeditor import CKEditor
from models import Portfolio, setup_db
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.abspath('templates')

    # Initialize the app
    app = Flask(__name__, template_folder=template_dir)

    # Load default config from settings.py
    app.config.from_pyfile('settings.py')

    # Initialize Plugins
    CORS(app, resources={r"*": {"origins": "*"}})
    CKEditor(app)

    # Initialize database
    setup_db(app)

    # Config MySQL (Already managed via settings.py)
    app.config['MYSQL_PORT'] = 3306
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    # Landing page
    @app.route('/')
    def landing_page():
        return redirect(url_for('view_portfolio'))

    # Portfolio page (GET only, no POST here)
    @app.route('/portfolio', methods=['GET'])
    def view_portfolio():
        portfolio = Portfolio.query.first()  # Load portfolio
        return render_template('pages/portfolio.html', portfolio=portfolio)

    # Update portfolio (POST allowed)
    @app.route('/portfolio/update/', methods=['GET', 'POST'])
    def update_portfolio():
        # Load the portfolio
        portfolio = Portfolio.query.first()

        if request.method == 'POST':
            # Process form data directly from request.form
            name = request.form.get('name')
            title = request.form.get('title')
            bio = request.form.get('bio')
            email = request.form.get('email')
            linkedin_link = request.form.get('linkedin_link')
            github_link = request.form.get('github_link')
            cv_link = request.form.get('cv_link')
            profile_picture_url = request.form.get('profile_picture_url')  # Get image link directly from form

            # Update the portfolio data
            portfolio.name = name
            portfolio.title = title
            portfolio.bio = bio
            portfolio.email = email
            portfolio.linkedin_link = linkedin_link
            portfolio.github_link = github_link
            portfolio.cv_link = cv_link
            portfolio.profile_picture_url = profile_picture_url  # Update profile picture URL

            portfolio.update()  # Update in the database
            flash('Portfolio updated successfully!', 'success')
            return redirect(url_for('view_portfolio'))

        return render_template('pages/update_portfolio.html', portfolio=portfolio)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
