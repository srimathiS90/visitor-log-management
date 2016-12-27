''' Importing all the modules'''
from flask import Flask, render_template,request,flash
from forms import RegistrationForm
import sqlite3 as sql
import xlwt
from models import insert_visitor

app = Flask(__name__) 
app.secret_key = 'development key'  
@app.route('/')
def layout():
  return render_template('layout.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/visitorregistration',methods=['GET','POST'])
def visitorregistration():
  form = RegistrationForm()
 
  if request.method == 'POST':
      
      if form.validate() == False:
        flash('All fields are required.')
        return render_template('visitorregistration.html', form=form)
      else:
          insert_visitor(request.form['firstname'],request.form['lastname'],request.form['email'],request.form['phoneno'],request.form['visiting'])
          return render_template('layout.html')
 
  elif request.method == 'GET':
    return render_template('visitorregistration.html', form=form)


 #Fetching all the visitor information from the database and creating a excel file        
@app.route('/allvisitors')
def allvisitors():
    
    con = sql.connect("test.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from visitorstable3")
    rows=cur.fetchall();
    print rows 
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')
    
    ws.write(0, 0, 'FirstName')
    ws.write(0, 1, 'LastName')
    ws.write(0, 2, 'Email ID')
    ws.write(0, 3, 'Mobile No.')
    ws.write(0, 4, 'Visiting')
    
    [ws.write(i+1, j, row[j]) for i, row in enumerate(rows) for j, value in enumerate(row) ]            
    wb.save('srimathi.xls')
    return render_template("allvisitors.html",rows = rows)
    
@app.route('/export_excel')
def export_excel():
    
    return render_template('export_excel.html')
	   
if __name__ == '__main__':
   
    app.run(debug=True)