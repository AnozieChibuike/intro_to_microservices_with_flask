from FlaskSQLAlchemyBaseModel import BaseModel, db

class Todo(BaseModel):
    __tablename__ = 'todos'
    user_id = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.task}>'