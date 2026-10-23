#!/usr/bin/python3
"""Simple API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object of the given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the JSON request body."""
    user = request.get_json(silent=True)
    if not isinstance(user, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    username = user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
