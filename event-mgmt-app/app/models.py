from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Event('{self.title}')"

