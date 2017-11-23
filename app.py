from flask import Flask, jsonify, render_template
from flasgger import Swagger, swag_from

from services.logger import AppLogger

app = Flask(__name__)
swagger = Swagger(app)
logger = AppLogger('myapp', 'app.log').get_logger()


@app.route('/<name>')
@swag_from('./apidocs/hello_world.yml')
def hello_world(name):
    logger.info('hello {}'.format(name))
    return jsonify({"my_name":name})


@app.route('/template/<name>')
def template(name):
    return render_template('index.html', name=name)
