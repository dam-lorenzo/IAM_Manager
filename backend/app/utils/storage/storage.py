from typing import Tuple
from flask import jsonify

from ...models.api_models import AccessCreate, AccessResponse, ServiceCreate, UserCreate, UserResponse, RoleCreate, RoleResponse
from pydantic import ValidationError
from ...utils.logger import get_logger
from ...storage.access_dao import access_dao
from ...storage.user_dao import user_dao
from ...storage.service_dao import service_dao
from ...storage.role_dao import role_dao

logger = get_logger()

def create_user(raw_data: dict) -> Tuple[dict, int]:
    """_summary_

    Args:
        raw_data (dict): _description_

    Returns:
        Tuple[dict, int]: _description_
    """
    try:
        user_data = UserCreate(**raw_data)
    except ValidationError as e:
        logger.error(f"Validation error while creating user: {e.errors()}")
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


def create_service(raw_data: dict) -> Tuple[dict, int]:
    """_summary_

    Args:
        raw_data (dict): _description_

    Returns:
        Tuple[dict, int]: _description_
    """
    try:
        user_data = ServiceCreate(**raw_data)
    except ValidationError as e:
        logger.error(f"Validation error while creating user: {e.errors()}")
        return jsonify({"message": "Validation errors", "errors": e.errors()}), 400

    try:
        # Search for duplicates 
        existing_user = service_dao.get_by_email(user_data.email)
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


def create_access(raw_data:dict) -> dict | int:
    try:
        access_data = AccessCreate(**raw_data)
    except ValidationError as e:
        logger.error(f"Validation error while creating user: {e.errors()}")
        return jsonify({"message": "Validation errors", "errors": e.errors()}), 400

    try:
        # Search for duplicates 
        existing_acess = access_dao.get_by_email(access_data.email)
        if existing_acess:
            logger.debug(f"Attempt to create duplicate user with email: {access_data.email}")
            return jsonify({"message": "A user with that email already exists"}), 409

        # We use .model_dump() to pass a clean dictionary to the DAO
        new_user_orm = service_dao.create(access_data.model_dump())
        
        #UserResponse schema to safely format the output
        response_data = AccessResponse.model_validate(new_user_orm)

        logger.info(f"User created successfully with ID: {response_data.id}")
        
        return response_data.model_dump_json(), 201

    except Exception as e:
        # Catch any other error (e.g., DB connection failure)
        logger.error(f"Unexpected error while creating user: {e}")
        return jsonify({"message": "An error occurred on the server"}), 500


def create_role(raw_data:dict) -> (dict, int):
    try:
        role_data = RoleCreate(**raw_data)
    except ValidationError as e:
        logger.error(f"Validation error while creating user: {e.errors()}")
        return jsonify({"message": "Validation errors", "errors": e.errors()}), 400

    try:
        # Search for duplicates 
        existing_role = access_dao.get_by_email(role_data.email)
        if existing_role:
            logger.debug(f"Attempt to create duplicate user with email: {role_data.email}")
            return jsonify({"message": "A user with that email already exists"}), 409

        # We use .model_dump() to pass a clean dictionary to the DAO
        new_user_orm = role_dao.create(role_data.model_dump())
        
        #UserResponse schema to safely format the output
        response_data = RoleResponse.model_validate(new_user_orm)

        logger.info(f"User created successfully with ID: {response_data.id}")
        
        return response_data.model_dump_json(), 201

    except Exception as e:
        # Catch any other error (e.g., DB connection failure)
        logger.error(f"Unexpected error while creating user: {e}")
        return jsonify({"message": "An error occurred on the server"}), 500
