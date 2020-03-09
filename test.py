from flask import render_template, Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# @app.route('/hello/')
# def hello(name=None):
#     return render_template('hello.html', name=name)

class HelloWorld(Resource):
    def get(self):
        return render_template('main.html', name=name)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 80)