from flasksqlalchemybasemodel import BaseModel, db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class User(BaseModel):
    __tablename__ = 'users'
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.save()  # Save the user instance after setting the password hash
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'