from api.extensions import db
import secrets


def hexid():
    return secrets.token_hex(8)

class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.String(100), primary_key=True, default=hexid)
    book