from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped['int'] = sa.mapped_column(primary_key=True)
    username: so.Mapped[str] = sa.mapped_column(sa.string(64), unique=True, index=True)
    email: so.Mapped[str] = sa.mapped_column(sa.sring(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = sa.column(sa.string(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
                                                    
