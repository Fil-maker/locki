from api import db
from api.models.users import Roles


class UsersToLibraries(db.Model):
    __tablename__ = "users_to_libraries"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    document_id = db.Column(db.Integer(), db.ForeignKey("libraries.id"))

    role = db.Column(db.Integer(), default=Roles.NO_ROLE.value)

    library = db.relationship("Library", back_populates="users")
    user = db.relationship("User", back_populates="libraries")


class Library(db.Model):
    __tablename__ = "libraries"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    users = db.relationship("UsersToLibraries", back_populates="library")
