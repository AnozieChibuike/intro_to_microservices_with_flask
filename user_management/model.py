from flasksqlalchemybasemodel import BaseModel, db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import random
usernames: list = ["RoscoBear47","WildeBeest21","Achiever211","MundanePirate19", "FamousGator1122"]

def generateRandomUsername():
    return usernames[random.randint(0,(len(usernames) - 1))] 

class User(BaseModel):
    __tablename__ = 'users'
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    username=db.Column(db.String(128), default=generateRandomUsername)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.save()  # Save the user instance after setting the password hash
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'