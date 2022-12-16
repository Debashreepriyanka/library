from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__') #creating app object of flask class
@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="Debashree@556",database="library_management")
    
        cu=db.cursor()
        q="select* from detail"
        cu.execute(q)
        data=cu.fetchall()
        return render_template("Mainpage.html",d=data)
    

    except Exception as e:
        return("Error")    

    
@app.route('/create')
def create():
    return render_template("form.html")
@app.route('/store',methods=['POST'])
def store():
    b=request.form['b']
    a=request.form['a']
    pdt=request.form['pdt']
    avail=request.form['avail']
    try:
        db=pymysql.connect(host="localhost",user="root",password="Debashree@556",database="library_management")
   
        cu=db.cursor()
        
        q="insert into detail(bookname,Author,Published_date,Availability) values('{}','{}','{}','{}')".format(b,a,pdt,avail)
        cu.execute(q)
        db.commit()#commit is a function used to close database
        return redirect('/')
    except Exception as e:
        return("Error",+e)
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="Debashree@556",database="library_management")
        cu=db.cursor()
        q="delete from detail where id='{}'".format(rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    except Exception as e:
        
        return("Error")     
@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="Debashree@556",database="library_management")
        cu=db.cursor()
        q="select* from detail where Id='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template("editform.html",d=data)

    except Exception as e:
        return("Error") 
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    b=request.form['b']
    a=request.form['a']
    pdt=request.form['pdt']
    avail=request.form['avail']
    try:
        db=pymysql.connect(host="localhost",user="root",password="Debashree@556",database="library_management")
        cu=db.cursor()
        q="update detail SET bookname='{}',Author='{}',Published_date='{}',Availability='{}' where Id='{}'".format(b,a,pdt,avail,rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    except Exception as e:
        return("Error") 
    
    
    
app.run(debug=True)