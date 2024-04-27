from .db import db, environment, SCHEMA, add_prefix_for_prod

class File(db.Model):
    __tablename__ = 'files'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(40), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    user = db.relationship('User', back_populates='files')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.url,
            'type': self.type,
            'created_at': self.created_at,
        }
