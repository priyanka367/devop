from flask import Flask,request,render_template
app=Flask(_name_)
@app.route('/register',methods=['GET',POST])
def register():
if request.method== 'POST':
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    return render_template('sucess.html')
    return render_template('register.html')
    if__name__ == '__main__':
        app.run(host='0.0.0.0')