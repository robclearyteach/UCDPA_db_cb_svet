from models import db, Recipe
from sqlalchemy.exc import SQLAlchemyError
import logging

def add_recipe(title, ingredients, instructions, image_name):
    try:
        new_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, image_name=image_name)
        db.session.add(new_recipe)
        db.session.commit()
        logging.info(f"Added recipe: {title}")
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error adding recipe {title}: {str(e)}")
        raise SQLAlchemyError(f"Error adding recipe {title}: {str(e)}")

def get_recipe_by_title(title):
    return Recipe.query.filter_by(title=title).first()

def get_all_recipes():
    return Recipe.query.all()

def get_recipe(recipe_id):
    return Recipe.query.get(recipe_id)

def update_recipe(recipe_id, title, ingredients, instructions):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        recipe.title = title
        recipe.ingredients = ingredients
        recipe.instructions = instructions
        db.session.commit()

def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()

def search_recipes(search_term):
    search_term = f"%{search_term}%"
    return Recipe.query.filter(
        (Recipe.title.ilike(search_term)) | 
        (Recipe.ingredients.ilike(search_term))
    ).all()

def update_recipe_image(recipe_id, image_name):
    try:
        recipe = Recipe.query.get(recipe_id)
        if recipe:
            recipe.image_name = image_name
            db.session.commit()
            logging.info(f"Updated image for recipe ID {recipe_id}")
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error updating image for recipe ID {recipe_id}: {str(e)}")
        raise SQLAlchemyError(f"Error updating image for recipe ID {recipe_id}: {str(e)}")

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s:%(message)s')
