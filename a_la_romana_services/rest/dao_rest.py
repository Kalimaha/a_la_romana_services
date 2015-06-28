import json
from flask import Blueprint
from flask import request
from flask import Response
from bson import json_util
from flask.ext.cors import cross_origin
from a_la_romana_services.core.dao import DAO
from a_la_romana_services.config.settings import config
from a_la_romana_services.config.settings import test_config


dao_rest = Blueprint('dao_rest', __name__)


@dao_rest.route('/users/<config>/', methods=['GET'])
@cross_origin(origins='*', headers=['Content-Type'])
def get_users(config):
    dao = DAO(config) if config is None else DAO(test_config)
    users = json.dumps([_user for _user in dao.get_user(None)],
                       sort_keys=True,
                       indent=4,
                       default=json_util.default)
    return Response(users, content_type='application/json; charset=utf-8')


@dao_rest.route('/users/<config>/', methods=['POST'])
@cross_origin(origins='*', headers=['Content-Type'])
def create_usr(config):
    dao = DAO(config) if config is None else DAO(test_config)
    user = json.loads(request.data)
    user_id = dao.create_user(user)
    users = json.dumps(user_id,
                       sort_keys=True,
                       indent=4,
                       default=json_util.default)
    return Response(users, content_type='application/json; charset=utf-8')
