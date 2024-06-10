import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "..","shared","app.db") # SHOULD POINT TO THE SHARED FOLDER

class Config:
    SECRET_KEY = "This should be something more secured" 
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path # We are using a test db for now, but we can change this to a production db later o
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    