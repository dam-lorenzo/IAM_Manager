import traceback
from flask import Blueprint, request, jsonify
from ..utils.logger import get_logger
from ..storage.access_dao import access_dao
from ..storage.user_dao import user_dao

logger = get_logger()

storage_bp = Blueprint("storage", __name__, url_prefix="/storage")

# GET /api/storage - Get all users
@storage_bp.route("/all", methods=["GET"])
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
        logger.error(f"Error getting accesses: {e}")
        return jsonify({"error": "An error occurred on the server"}), 500

# GET /api/storage/<id> - Get access by user ID
@storage_bp.route("search/<table>", methods=["GET"])
def get_user(table):
    logger.debug(f"search/{table}")
    try:
        match table:
            case "accesses":
                info_db = access_dao.get_all(request.args)
            case "users":
                info_db = user_dao.get_all(request.args)
        if isinstance(info_db,list):
            result = [record.to_dict() for record in info_db]
        else:
            result = [info_db.to_dict()]
        if not result:
            return jsonify({"Message": "User not found"}), 404
        return jsonify(result), 200
    except AttributeError as e:
        return jsonify({"Message": "Bad query parameters"}), 400
    except Exception as e:
        # Basic error handling
        logger.error(f"Error getting accesses: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"Error": "An error occurred on the server"}), 500


# POST /api/storage - Create a new user
@storage_bp.route("/create_user", methods=["POST"])
def create_user():
    raw_data = request.get_json()
    if not raw_data:
        return jsonify({"Message": "Invalid payload"}), 400
    logger.debug(raw_data)
    data = {
        "full_name": raw_data.get("full_name"),
        "email": raw_data.get("email")
    }
    search_result = user_dao.get_all(filters=data)
    if search_result:
        logger.debug("Duplicated user")
        return jsonify({"Message": "User already exists"}), 409
    result = user_dao.create(data)
    logger.debug(result)
    return jsonify({"Message": "User created"}), 201


# PUT /api/storage/<id> - Update a user
@storage_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    logger.debug(data)
    return jsonify({"Message": "WIP"}), 201