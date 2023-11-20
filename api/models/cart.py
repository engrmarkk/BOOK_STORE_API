from api.extensions import db
import secrets


def hexid():
    return secrets.token_hex(8)


class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.String(100), primary_key=True, default=hexid)
    book = db.Column(db.String(100), db.ForeignKey('books.id'), nullable=False)
    user = db.Column(db.String(100), db.ForeignKey('users.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return f"Cart('{self.book}', '{self.user}', '{self.quantity}')"
