from extensions import db, app, login_manager
from flask_login import UserMixin

class BaseModel:
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def save(self):
        db.session.commit()


class User(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Product(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    img = db.Column(db.String)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

