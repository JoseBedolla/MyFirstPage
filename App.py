from flask import Flask, render_template

app = Flask(__name__)


# PAGINA HOME
@app.route('/')
def Index():
    return render_template('home.html')

# PAGINA ABOUT ME
@app.route('/about')
def About():
    return render_template('About.html')

# PAGINA DONDE SE VERAN LOS PROYECTOS
@app.route('/projects')
def Projects():
    return render_template('Projects.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)