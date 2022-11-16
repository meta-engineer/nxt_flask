from flask import Blueprint

# directories are relative to flask_app/
api = Blueprint('api_blueprint', __name__, url_prefix='/api', template_folder='api_blueprint/templates')
root = Blueprint('root_blueprint', __name__, template_folder='root_blueprint/templates')