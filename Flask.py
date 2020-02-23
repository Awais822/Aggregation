from flask import Flask,redirect,url_for,request,render_template
app = Flask(__name__,template_folder='template')
@app.route('/hello')
def hello_world():
    dict = {"physics":70,"Che":90,"Bio":90}
    return render_template('hello.html',result=dict)
'''@app.route("/success/<name>")
def success(name):
    return "Working with Flask @ %s!" %name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))'''

#app.add_url_rule("/","hello",hello_world)
if __name__ == '__main__':
    app.run(debug=True)



