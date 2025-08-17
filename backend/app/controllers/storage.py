from flask import Blueprint, request, jsonify
from ..utils.logger import get_logger

logger = get_logger()

storage_bp = Blueprint("storage", __name__, url_prefix="/storage")

# GET /api/storage - Get all users
@storage_bp.route("/", methods=["GET"])
def get_users():
    return jsonify([{"id": 1, "username": "prueba", "email": "prueba@prueba.com"}])


# GET /api/storage/<id> - Get a user by ID
@storage_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = None
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify([{"id": 1, "username": "prueba", "email": "prueba@prueba.com"}])


# POST /api/storage - Create a new user
@storage_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    logger.debug(data)
    return jsonify({"Message": "WIP"}), 201


# PUT /api/storage/<id> - Update a user
@storage_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    logger.debug(data)
    return jsonify({"Message": "WIP"}), 201