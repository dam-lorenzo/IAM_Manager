import traceback
from flask import Blueprint, request, jsonify
from ..models.api_models import UserCreate,UserResponse
from pydantic import ValidationError
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
            return jsonify({"message": "User not found"}), 404
        return jsonify(result), 200
    except AttributeError as e:
        return jsonify({"message": "Bad query parameters"}), 400
    except Exception as e:
        # Basic error handling
        logger.error(f"error getting accesses: {e}")
        logger.error(traceback.format_exc())
        return jsonify({"error": "An error occurred on the server"}), 500


# POST /api/storage - Create a new user

@storage_bp.route("/create_user", methods=["POST"])
def create_user():
    """
    Creates a new user by validating the input data.
    """
    raw_data = request.get_json()
    if not raw_data:
        return jsonify({"message": "Request body cannot be empty"}), 400

    #Pydantic
    try:
        user_data = UserCreate(**raw_data)
    except ValidationError as e:
        logger.warning(f"Validation error while creating user: {e.errors()}")
        return jsonify({"message": "Validation errors", "errors": e.errors()}), 400

    try:
        # Search for duplicates 
        existing_user = user_dao.get_by_email(user_data.email)
        if existing_user:
            logger.debug(f"Attempt to create duplicate user with email: {user_data.email}")
            return jsonify({"message": "A user with that email already exists"}), 409

        # We use .model_dump() to pass a clean dictionary to the DAO
        new_user_orm = user_dao.create(user_data.model_dump())
        
        #UserResponse schema to safely format the output
        response_data = UserResponse.model_validate(new_user_orm)

        logger.info(f"User created successfully with ID: {response_data.id}")
        
        return response_data.model_dump_json(), 201

    except Exception as e:
        # Catch any other error (e.g., DB connection failure)
        logger.error(f"Unexpected error while creating user: {e}")
        return jsonify({"message": "An error occurred on the server"}), 500

# PUT /api/storage/<id> - Update a user
@storage_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    logger.debug(data)
    return jsonify({"Message": "WIP"}), 201