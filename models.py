from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    published = Column(DateTime(timezone=True), nullable=False)
    content = Column(String, nullable=True)
    image = Column(String, nullable=True)

    def json(self):
        return {
            "id":str(self.id),
            "title":self.title,
            "author":self.author,
            "published":str(self.published),
            "content":self.content,
            "image":self.image,
        }

    def __repr__(self):
        return '<News {}>'.format(self.title)
