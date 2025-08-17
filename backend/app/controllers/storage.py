from flask import Blueprint, request, jsonify
from ..utils.logger import get_logger
from ..storage.access_dao import access_dao

logger = get_logger()

storage_bp = Blueprint("storage", __name__, url_prefix="/storage")

# GET /api/storage - Get all users
@storage_bp.route("/", methods=["GET"])
def get_all_accesses():
    """
    Gets a list of all accesses, with nested information
    of the associated user, service, and role.
    """
    try:
        # 1. Use your DAO to get all objects from the database
        all_access_records = access_dao.get_all()
        
        # 2. Use a list comprehension to convert each object to a dictionary
        #    using the to_dict() method defined in the model.
        result = [record.to_dict() for record in all_access_records]
        
        # 3. Return the list of dictionaries in JSON format
        return jsonify(result), 200
        
    except Exception as e:
        # Basic error handling
        print(f"Error getting accesses: {e}")
        return jsonify({"error": "An error occurred on the server"}), 500

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