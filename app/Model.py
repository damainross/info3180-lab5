import datetime
#from flask_sqlalchemy import SQLAlchemy
#from app import app
from . import db
 







class User(db.Model):

     


    id = db.Column(db.Integer, primary_key=True)

    f_name = db.Column(db.String(80), unique=False, nullable=False)  #

    l_name = db.Column(db.String(80), unique=False, nullable=False) #

    gender = db.Column(db.String(6), nullable=True)#
    
    email = db.Column(db.String(80), unique=True)
    
    location = db.Column(db.String(80), unique=False)
    
    biography  = db.Column(db.String(200), unique=False)

    profile_picture = db.Column(db.String(100), nullable=True)


    created_on = db.Column(db.DateTime, nullable=True,default=datetime.datetime.now())



    def __init__(self,  f_name, l_name,email,location,biography,gender,profile_picture):


        self.f_name = f_name

        self.l_name = l_name

        self.email = email
        self.location = location
        self.biography = biography
        
        self.gender = gender
        self.profile_picturee=profile_picture
        
        
        
         
        #self.user_id = User.generate_user_id()
  
    
    
    
    
    
     
    
    
    def __repr__(self):

        return '<id {}>'.format(self.id)
