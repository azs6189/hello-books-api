# Blueprint is a Flask class that provides a pattern for grouping related routes(endpoints)
from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)
