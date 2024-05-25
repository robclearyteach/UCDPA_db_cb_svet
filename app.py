from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Recipe, User
from database import add_recipe, get_recipe, update_recipe, delete_recipe, search_recipes, update_recipe_image
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, RecipeForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import logging

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Select database configuration based on the runtime environment
if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object('config.PostgreSQLConfig')
else:
    app.config.from_object('config.SQLiteConfig')

app.config['UPLOAD_FOLDER'] = 'static/images/'  # Folder for uploading images
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12345')
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create all tables in the database
with app.app_context():
    db.create_all()

@app.context_processor
def inject_forms():
    return dict(login_form=LoginForm(), register_form=RegisterForm())

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = get_recipe(recipe_id)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    else:
        return "Recipe not found", 404

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_recipe_route():
    form = RecipeForm()
    if form.validate_on_submit():
        title = form.title.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data

        if 'image' in request.files:
            image_name = store_image(request.files['image'])
        try:
            add_recipe(title, ingredients, instructions, image_name)
            return redirect(url_for('index'))
        except Exception as e:
            return render_template('add_recipe.html', form=form, error_message=str(e))

    return render_template('add_recipe.html', form=form)

def store_image(image):
    image = request.files['image']
    image_name = image.filename if image.filename else 'default_image.jpg'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    image.save(os.path.join(upload_folder, image_name))
    return image_name


@app.route('/update/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def update_recipe_route(recipe_id):
    recipe = get_recipe(recipe_id)
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        title = form.title.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data
        update_recipe(recipe_id, title, ingredients, instructions)

        if 'image' in request.files:
            image_name = store_image(request.files['image'])
            update_recipe_image(recipe_id, image_name)

        return redirect(url_for('index'))

    return render_template('update_recipe.html', form=form, recipe=recipe)

@app.route('/delete/<int:recipe_id>', methods=['POST'])
@login_required
def delete_recipe_route(recipe_id):
    delete_recipe(recipe_id)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        recipes = search_recipes(search_term)
        return render_template('search.html', recipes=recipes)
    return render_template('search.html', recipes=[])

@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('You have successfully registered!', 'success')
        return jsonify({'success': True})
    return jsonify({'success': False, 'errors': form.errors})

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return jsonify({'success': True})
        return jsonify({'success': False, 'errors': {'login': ['Invalid username or password']}})
    return jsonify({'success': False, 'errors': form.errors})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/is_logged_in')
def is_logged_in():
    return jsonify({'logged_in': current_user.is_authenticated})

if __name__ == '__main__':
    app.run(debug=True, port=8000)




"""
            image = request.files['image']
            image_name = image.filename if image.filename else 'default_image.jpg'
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            image.save(os.path.join(upload_folder, image_name))

"""