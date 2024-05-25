# Culinary Recipes Website https://recipe-app-web.onrender.com

This website is a culinary portal where users can register, add, edit, and delete recipes, as well as search for recipes by ingredients.

## Project Structure

### Main Idea
The site allows users to interact with recipes in various ways, including adding new recipes, updating existing ones, deleting them, and searching for recipes based on ingredients.

### Files and Their Functions

1. **app.py**
   - This is the main Flask application file. It sets up routes, logging, and database connections.
   - Defined routes:
     - `/` - Display the home page.
     - `/recipe/<int:recipe_id>` - View recipe details.
     - `/add` - Add a new recipe.
     - `/update/<int:recipe_id>` - Update a recipe.
     - `/delete/<int:recipe_id>` - Delete a recipe.
     - `/search` - Search for recipes.
     - `/register` - Register a new user.
     - `/login` - User login.
     - `/logout` - User logout.

2. **config.py**
   - Contains configurations for the database and other settings. Depending on the environment (production or development), it chooses the configuration for PostgreSQL or SQLite.

3. **create_user.py**
   - Script for creating a new user in the database. Used for administration purposes.

4. **database.py**
   - Contains functions for interacting with the database:
     - Adding, retrieving, updating, and deleting recipes.
     - Searching for recipes by ingredients.
     - Updating recipe images.

5. **forms.py**
   - Defines web interface forms using Flask-WTF:
     - `RecipeForm` - Form for adding and editing recipes.
     - `LoginForm` - Form for user login.
     - `RegisterForm` - Form for user registration.

6. **models.py**
   - Defines database models using SQLAlchemy:
     - `User` model.
     - `Recipe` model.

7. **HTML Templates (in the templates folder)**
   - **base.html**: The main template that contains the common structure of the page (header, navigation, footer). Other templates extend this one.
   - **add_recipe.html**: Template for the add recipe page.
   - **card_form.html** and **index.html**: Templates for displaying the home page and recipes in a card format.
   - **recipe_detail.html**: Template for displaying detailed information about a recipe.
   - **recipe.html**: Template for displaying a specific recipe.
   - **search.html**: Template for the search page.
   - **update_recipe.html**: Template for the update recipe page.

8. **Static Files (in the static folder)**
   - **style.css**: Styles for the website.
   - **main.js**: Script for handling modals for login and registration, and processing login and registration forms.

### User Flow Example

1. **Home Page**
   - The user lands on the home page and sees a list of recipes. Each recipe is displayed as a card.
   - Clicking on a recipe leads to the recipe details page.

2. **Registration and Login**
   - If the user is not logged in and wants to add a recipe, they click on the "Add Recipe" button. A modal window for login or registration appears.
   - After successful registration or login, the user can add recipes.

3. **Adding a Recipe**
   - The user fills out the form to add a recipe (entering the title, ingredients, instructions, and uploading an image).
   - The form is submitted to the server, and the data is saved in the database.

4. **Editing and Deleting a Recipe**
   - On the recipe detail page, the user can click "Edit" to edit the recipe or "Delete" to delete it.
   - During editing, the user sees a form pre-filled with the current recipe data and can make changes.

5. **Searching for Recipes**
   - The user can search for recipes by ingredients. They enter ingredients in the search bar and get a list of matching recipes.

### File Interactions

- **HTML Templates** are rendered using Flask and Jinja2. They receive data from functions in `app.py`.
- **Forms** from `forms.py` are used to create and validate user input.
- **Database functions** from `database.py` are used to interact with the database.
- **Data models** from `models.py` represent the structure of the database tables.
- **Configuration files** from `config.py` define application settings.
- **Static files** (CSS and JS) provide styling and functionality on the client side.

Together, these files work to provide the site's functionality, from displaying recipes to managing users and interacting with the database.

## Contributors

- [Svetlana Melichova][(https://github.com/Svetlaniukas/recipe_app)] - Developer

## License

This project is licensed under the [MIT License](LICENSE).
# recipe_app
# recipe_app
