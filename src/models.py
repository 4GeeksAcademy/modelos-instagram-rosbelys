from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

db = SQLAlchemy()

class MediaType(enum.Enum):
    IMAGE = "image"

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)


    def serialize(self):
        return{
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
            
        }
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return{
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id
        }

class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)
    url: Mapped[str] = mapped_column(String(120), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("userid"))

    def serialize(self):
        return{
            "id": self.id,
            "type": self.type.value,
            "url": self.url,
            "post_id": self.post_id
        }
    
if __name__ == "__main__":
    db.create_all()


