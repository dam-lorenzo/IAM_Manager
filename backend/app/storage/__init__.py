# app/data_access/base_dao.py
from ..extensions import db

class BaseDAO:
    def __init__(self, model):
        """
        Initializes the DAO with a specific SQLAlchemy model.

        Args:
            model: The SQLAlchemy model class this DAO will manage.
        """
        self.model = model

    def create(self, data):
        """
        Creates a new record in the database.

        Args:
            data (dict): A dictionary containing the fields for the new record.

        Returns:
            The newly created model instance.
        """
        instance = self.model(**data)
        db.session.add(instance)
        db.session.commit()
        return instance

    def get_by_id(self, id):
        """
        Retrieves a record by its primary key.

        Args:
            id: The primary key of the record.

        Returns:
            The model instance if found, otherwise None.
        """
        return self.model.query.get(id)
    
    def get_by_email(self, email):
        """
        Retrieves a record by its email.

        Args:
            email: email of the record.

        Returns:
            The model instance if found, otherwise None.
        """
        return self.model.query.get(email)

    def get_all(self, filters=None):
        """
        Retrieves all records that match the optional filters.

        Args:
            filters (dict, optional): A dictionary of filters to apply,
                                      where key is the field and value is the value.
                                      Defaults to None.

        Returns:
            A list of matching model instances.
        """
        query = self.model.query
        if filters:
            for field, value in filters.items():
                query = query.filter(getattr(self.model, field) == value)
        return query.all()

    def update(self, id, data):
        """
        Updates an existing record by its primary key.

        Args:
            id: The primary key of the record to update.
            data (dict): A dictionary with the fields to modify.

        Returns:
            The updated model instance, or None if the record was not found.
        """
        instance = self.get_by_id(id)
        if not instance:
            return None
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance

    def delete(self, id):
        """
        Deletes a record by its primary key.

        Args:
            id: The primary key of the record to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        instance = self.get_by_id(id)
        if not instance:
            return False
        db.session.delete(instance)
        db.session.commit()
        return True