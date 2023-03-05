from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')
print(app.static_folder)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()



    







