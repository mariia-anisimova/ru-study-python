from typing import Union, Any

from flask import Flask, request, jsonify, make_response, abort
import json
from http import HTTPStatus



class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """



    @staticmethod
    def configure_routes(app: Flask) -> None:
        users_dict = {}

        @app.route('/user', methods=['POST'])
        def post_user() -> Union[tuple[Any, HTTPStatus], Any]:
            data_req = request.get_json()
            if "name" not in data_req:
                return jsonify({"errors": {"name": "This field is required"}}), 422
            user_name = data_req["name"]
            users_dict[user_name] = {}
            return jsonify(data=f"User {user_name} is created!"), 201

        @app.route("/user/<name>", methods=['GET'])
        def get_user(name) -> Union[tuple[Any, HTTPStatus], Any]:
            if name not in users_dict:
                abort(404)
            return jsonify(data=f"My name is {name}")

        @app.route("/user/<name>", methods=['PATCH'])
        def patch_user(name) -> Union[tuple[Any, HTTPStatus], Any]:
            if name not in users_dict:
                abort(404)
            new_name = request.json['name']
            users_dict[new_name] = users_dict.pop(name)
            return jsonify(data=f"My name is {new_name}")

        @app.route("/user/<name>", methods=['DELETE'])
        def delete_user(name) -> Union[tuple[Any, HTTPStatus], Any]:
            if name not in users_dict:
                abort(404)
            users_dict.pop(f"{name}")
            return "", 204


