#Validating all the form fields using wtforms
from flask_wtf import Form
from wtforms import  TextField, SubmitField,validators


class RegistrationForm(Form):
  firstname = TextField("FirstName", [validators.DataRequired("Please enter your firstname")])
  lastname = TextField("LastName", [validators.DataRequired("Please enter your lastname")])
  email = TextField("Email", [validators.DataRequired("Please enter your email address"),validators.Email("Please enter your email address")])
  phoneno = TextField("MobileNumber", [validators.DataRequired("Please enter your mobile number"), validators.Regexp('^[0-9]+$', message="Mobile number must only contain integer values")])
  visiting = TextField("Visiting", [validators.DataRequired("Please enter the name of the person you are visiting")])
  
  submit = SubmitField("Register Visitor")