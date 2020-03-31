from flask import request, jsonify
from werkzeug.exceptions import HTTPException

from .. import db
from . import main
from ..models import Mendeley, Altmetrics, Bibliometrics
from sqlalchemy.sql import text

import logging
log = logging.getLogger()

table_map = {
    'bibliometrics': Bibliometrics,
    'altmetrics': Altmetrics,
    'mendeley': Mendeley,
}

@main.route('/')
def home():
    return 'Hello :)'


@main.route('/<table>/record/<id>', methods=['GET'])
def get_record(table, id):
    try:
        field = 'doi'
        if table == 'bibliometrics':
            field = 'issn1'
        table = table_map[table]
        data = table.query.filter(getattr(table, field) == id).all()
    except Exception as e:
        return jsonify(success='False', msg=f"Something wrong with the request", error=e)

    if len(data) > 0:
        return jsonify(data[0].as_dict())
    return jsonify(success='False', msg=f"Couldn't find record for {id}")


@main.errorhandler(HTTPException)
def handle_error(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response, e.code
