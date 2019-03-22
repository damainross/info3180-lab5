from flask_wtf import FlaskForm
#from wtforms import StringField,Form,validators,SubmitField
from wtforms.validators import DataRequired,Email
from wtforms import StringField,TextField
from wtforms import StringField, IntegerField, FileField, SelectField
from wtforms.validators import InputRequired
genders = {

    '0': 'male',

    '1': 'female'
    
}
#validators=[InputRequired()]
#validators=[DataRequired()]
SEX = list((k, v) for k, v in genders.items())
#SEX = ['male','female']
class create_profile(FlaskForm):
    f_name = StringField(u'first name',validators=[DataRequired()])
    l_name = StringField(u'last name',validators=[DataRequired()])
    gender = SelectField(u'gender', choices=SEX)
    email    = StringField(u'email',validators= [DataRequired(),Email()])
    location = StringField(u'location',validators=[DataRequired()])
    biography  = TextField(u'biography',validators=[DataRequired()])
    profile_picture = FileField(u'profile picture',validators=[DataRequired()])
      