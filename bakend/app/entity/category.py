from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.database_connectivity import Base


class Category(Base):
    __tablename__ = 'categories'
    color = Column(String(20))
    icon = Column(String(60))
    title = Column(String(40))
    user_id = Column(ForeignKey("user.id"))
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self, color, icon, title, user_id):
        self.color = color
        self.icon = icon
        self.title = title
        self.user_id = user_id
        self.id = None
