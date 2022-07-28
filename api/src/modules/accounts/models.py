import datetime
import jwt
import logging
from src.extensions import db, bcrypt
from sqlalchemy_utils import Timestamp
from flask import current_app

log = logging.getLogger(__name__)


class Accounts(db.Model, Timestamp):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    accountnumber = db.Column(db.String(128), nullable=False, unique=True)
    # password = db.Column(db.String(255), nullable=False)
    # email = db.Column(db.String(128), unique=True)
    # admin = db.Column(db.Boolean, default=False, nullable=False)
    # active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self,
                 accountnumber: str):
        self.accountnumber = acccountnumber

    def to_json(self):
        return {
            'id': self.id,
            'accountnumber': self.accountnumber,
        }