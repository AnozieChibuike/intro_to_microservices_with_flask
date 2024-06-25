from flasksqlalchemybasemodel import BaseModel, db


class Todo(BaseModel):
    __tablename__ = "todos"
    user_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), default="")
    task = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    tags = db.Column(db.JSON)
    due = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Todo {self.task}>"
