# coding: utf-8
# !/usr/bin/python3

import wrapper
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/test")
def hello():
    return "Hello World!"


@app.route('/api/v1/user/post', methods=['POST'])
def create_user():
    payload = request.form.to_dict()
    result = wrapper.User.add_user(**payload)
    if result:
        return jsonify(status='True', message='User created')
    return jsonify(status='False')


@app.route('/api/v1/user/', methods=['GET'])
def get_all_users():
    result = wrapper.get_all_users()
    if result:
        return jsonify(status="True",
                       result=[
                           {"nom": user.nom,
                            "prenom": user.prenom,
                            "email": user.email,
                            "telephone": user.telephone} for user in result.all()])
    return jsonify(status="False")


@app.route('/api/v1/user/<email>', methods=['GET'])
def get_user(email):
    result = wrapper.get_user_by_id(email)
    if result:
        return jsonify(status="True",
                       result={"nom": result.nom,
                               "prenom": result.prenom,
                               "email": result.email,
                               "telephone": result.telephone}
                       )
    return jsonify(status="False")


@app.route('/api/v1/user/&amp;amp;amp;amp;lt;email&amp;amp;amp;amp;gt;', methods=['PUT'])
def mofify_user(email):
    result = wrapper.update_attribute(email, request.form.to_dict())

    if result:
        return jsonify(status="True",
                       message="updated",
                       result={
                           "nom": result.nom,
                           "prenom": result.prenom,
                           "email": result.email,
                           "telephone": result.telephone}
                       )
    return jsonify(status="False")


@app.route('/api/v1/user/&amp;amp;amp;amp;lt;email&amp;amp;amp;amp;gt;', methods=['DELETE'])
def delete_user(email):
    result = wrapper.delete_user_by_id(email)
    if result:
        return jsonify(status="True",
                       message="Deleted",
                       email=email
                       )
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
