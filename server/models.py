from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 

    @validates('name')
    def validate_name(self,key,name):
        if name == '': 
            raise ValueError("Name cannot be empty.")
        return name
    
    @validates('phone_number')
    def validates_phone_number(self,key,phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must be ten digits.")
        return phone_number
    

        
    
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def validates_title(self,key,title):
        if title == '':
            raise ValueError("Post must have a title.")
        return title
    
    @validates('content')
    def validate_content(self,key,content):
        if len(content) > 250:
            raise ValueError("Content must be atleast 250 digits long.")
        return content
    
    @validates('category')
    def validates_category(self,key,category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Category must be Fiction or Non Fiction.")
        return category
    
    

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
