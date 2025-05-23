from app import db

class ProfileImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime)

    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))