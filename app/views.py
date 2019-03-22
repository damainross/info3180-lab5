#import os
#from app import app

#from werkzeug import secure_filename
#from flask import render_template, request, redirect, url_for, flash,jsonify
#from app.Model import User
#from .  import db
#from .form import create_profile
#from app import  db


from app import app

from flask import render_template, request, redirect, url_for,flash

from app import db

from app.Model import User

from flask import jsonify, session

from datetime import *

from  .form import create_profile

import json

from flask import Response

from werkzeug import secure_filename

import os











ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

 


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')




#def allowed_file(filename):

    #return '.' in filename and \

           #filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
           
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
           
           
           
@app.route('/profile',methods=['GET', 'POST'])
def profile():
  form = create_profile()
  #if request.method=='POST' and form.validate_on_submit():
      ##write to database
      
  if request.method == 'POST':
        
        if form.validate_on_submit():
            
   
            #form = create_profile(request.form)
            #id = form.username.data
            im = request.files['profile_picture']
            u = User(form.f_name.data,
            form.l_name.data,
            form.email.data,
            form.location.data,
            form.biography.data,
            form.gender.data,
            im.filename)
            #sex=form.gender.data
            db.session.add(u)
            db.session.commit()
            
            #uploaded_file = request.files['image']
            file = request.files['profile_picture']
            #fille = secure_filename(file.filename)
            if  file  and  allowed_file(file.filename):
                
                filename = 'file{0}'.format(
                    #this simply affilates each uploaded photo to the userid of the 'owner' of the photo 
                        u.id)
                f=secure_filename(filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],

                                                    f))

                u.profile_picture = filename

                db.session.commit()
                flash('successfully created')
                return redirect(url_for('profiles'))



      
  return render_template('new_profile.html',form=form)
  
@app.route('/profiles', methods=['GET', 'POST'])

def profiles():

    #users = User.query.all()
    users = db.session.query(User).all()

#users:#request.method == 'POST' and 
    if 1==1:#request.headers['Content-Type'] == 'application/json':
        #users = User.query.all()
        
        users_from_db = {}

        for user in users_from_db:
            #add users to dict
            users_from_db.update({

                'name': user.f_name+' '+user.l_name,

                'location': user.location

            })
        users_from_db.update({'name':'the','location':'somewhere'})

        #return jsonify(users_from_db)  #return all as dictionary for ease of access of results
    

    
    return render_template('profiles.html', user=users)
    
    
    
    
def get_uploaded_images():
    l=[]
    rootdir = os.getcwd()
    #print rootdir
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
           # os.path.join(subdir, file)
            l.append(file)
    return l
    
    
    
@app.route('/profile_detail/<int:user_id>')

def profile_detail(user_id):

    user = User.query.get(user_id)



    if not user:
        #return redirect(url_for('home'))
        return redirect(url_for('profiles'))



    else:
        #return redirect(url_for('home')) 
        return render_template('profile.html', user=user)
