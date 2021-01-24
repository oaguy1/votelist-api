"""
Just enough CRUD operations to get you going
"""
import hashlib

from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from app.db import models, schemas

""" These constants need to be moved to a config """
SALT = "This is my salt. There are many like it, but this one is mine."
HMAC_ITER = 100000


def get_user(db: Session, user_id: int):
    """Get a user by user id"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get us user by email"""
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users, takes an offset and limit"""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Store user in DB with hashed_password"""
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        user.password.encode('utf-8'),
        SALT.encode('utf-8'),
        HMAC_ITER
    )
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """Get all items, takes an offset and limit"""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """Store itme in the DB"""
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item