from flask import Blueprint


blueprint = Blueprint('web', __name__)


@blueprint.route('/')
def index():
    return 'Hello World'