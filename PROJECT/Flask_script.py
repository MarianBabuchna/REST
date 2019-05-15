from PROJECT import record_func
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


@app.route('/record', methods=['POST'])
def post_record():
    record_func.record_write_new_json("")
    return "POST_return"


@app.route('/record/<uuid>', methods=['GET'])
def get_record(uuid):
    return record_func.record_uuid_get(uuid)


@app.route('/record/<uuid>', methods=['DELETE'])
def delete_record(uuid):
    record_func.record_uuid_delete(uuid)
    return "DELETE_return"


@app.route('/record/<uuid>', methods=['PATCH'])
def patch_record(uuid):
    record_func.record_uuid_patch(uuid)
    return "PATCH_return"


app.run(debug=True)
