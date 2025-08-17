# backend/app/models/orm_models.py

from datetime import datetime
from ..extensions import db 
from . import BaseModel

class User(db.Model, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    accesses = db.relationship('Access', back_populates='user', lazy=True, cascade="all, delete-orphan")

class Service(db.Model, BaseModel):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    roles = db.relationship('Role', back_populates='service', lazy=True, cascade="all, delete-orphan")
    accesses = db.relationship('Access', back_populates='service', lazy=True)

class Role(db.Model, BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)

    service = db.relationship('Service', back_populates='roles')
    # Automatically deletes related records if a user is deleted
    accesses = db.relationship('Access', back_populates='role', cascade="all, delete-orphan")

class Access(db.Model, BaseModel):
    __tablename__ = 'accesses'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    user = db.relationship('User', back_populates='accesses')
    service = db.relationship('Service', back_populates='accesses')
    role = db.relationship('Role', back_populates='accesses')

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict() if self.user else None,
            'service': self.service.to_dict() if self.service else None,
            'role': self.role.to_dict() if self.role else None
        }