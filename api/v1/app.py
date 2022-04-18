#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""
Flask App that integrates with AirBnB static HTML Template
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from models import storage
import os
from werkzeug.exceptions import HTTPException

# Global Flask Application Variable: app
app = Flask(__name__)
swagger = Swagger(app)

# global strict slashes
app.url_map.strict_slashes = False

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
=======
'''
Starts the Flask web application
'''
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
=======
"""app.py to connect to API"""
import os
>>>>>>> 9dccf5970ec07ec7c5415959818d81926e3925d3
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_storage(exception):
    """Closes storage session"""
>>>>>>> f733036454d83cd38497b06d25298c5234071b04
=======
def teardown_appcontext(code):
    """teardown_appcontext"""
>>>>>>> 9dccf5970ec07ec7c5415959818d81926e3925d3
    storage.close()


@app.errorhandler(404)
<<<<<<< HEAD
<<<<<<< HEAD
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(400)
def handle_404(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(Exception)
def global_error_handler(err):
    """
        Global Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
    return make_response(jsonify(message), code)


def setup_global_errors():
    """
    This updates HTTPException Class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # initializes global error handling
    setup_global_errors()
    # start Flask app
    app.run(host=host, port=port)
=======
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    """Runs the app"""
    if environ.get('HBNB_API_HOST'):
        host = environ.get('HBNB_API_HOST')
    else:
        host = '0.0.0.0'

        if environ.get('HBNB_API_PORT'):
            port = environ.get('HBNB_API_PORT')
        else:
            port = 5000

        app.run(host=host, port=port, threaded=True)
>>>>>>> f733036454d83cd38497b06d25298c5234071b04
=======
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
>>>>>>> 9dccf5970ec07ec7c5415959818d81926e3925d3
