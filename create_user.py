from models import db, User
from werkzeug.security import generate_password_hash
from app import app

with app.app_context():
    try:
        # Create all tables in the database
        db.create_all()

        # Generate a hashed password
        hashed_password = generate_password_hash('yourpassword', method='pbkdf2:sha256')

        # Check if the user already exists
        existing_user = User.query.filter_by(username='yourusername').first()
        if existing_user:
            print("User already exists.")
        else:
            # Create a new user with the provided credentials
            new_user = User(username='yourusername', email='youremail@example.com', password=hashed_password)

            # Add the new user to the session and commit the changes to the database
            db.session.add(new_user)
            db.session.commit()
            print("User created successfully.")
    except Exception as e:
        # Print any errors that occur during the process
        db.session.rollback()  # Roll back the transaction in case of error
        print(f"An error occurred: {e}")

# run this script - ' python create_user.py '
