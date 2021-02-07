from flask import Flask, render_template
app = Flask(__name__)

def factors(num):
    return [x for x in range(1, num+1) if num%x==0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Garrett')
def garrett():
    return 'Hi Garrett!'

# lets pass dynamic information
@app.route('/Welcome/<name>')
def welcome_name(name):
    return "Welcome " + name + "!"

@app.route('/factor_raw/<int:n>')
def factors_display_raw(n):
    list_factor = factors(int(n))
    html = "<h1> Factors of "+str(n)+" are </h1>"+"\n"+"<ul>"
    for f in list_factor:
        html += "<li>"+str(f)+"</li>"+"\n"
    html += "</ul> </body>"
    return html


if __name__ == '__main__':
    app.run(debug=True)