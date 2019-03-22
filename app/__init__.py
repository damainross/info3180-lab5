#from flask import Flask

# Config Values
          
# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

 
'postgresql://znfpgnhgecphsq:4d427d1f68357dffa8ab06cff2653e29f2ae6f372d8a5d7cf2031f4b86143b18@ec2-23-23-195-205.compute-1.amazonaws.com:5432/dcj7u7458gp332'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#'postgresql://project1:project1@localhost/project1'
app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://project1:project1@localhost/project1'    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)

#app.config.from_object('config')



 
 



#app = Flask(__name__)
#app.config.from_object(__name__)
from app import views,Model
