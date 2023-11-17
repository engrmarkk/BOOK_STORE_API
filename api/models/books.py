from api.extensions import db
import secrets


def hexid():
    return secrets.token_hex(8)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(100), primary_key=True, default=hexid)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://res.cloudinary.com/duwyopabr/image/upload/v1676162283'
                                                       '/user_xz7o0f.png')
    description = db.Column(db.Text, nullable=False)
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
        return f"Book('{self.title}', '{self.author}', '{self.description}', '{self.quantity}')"
