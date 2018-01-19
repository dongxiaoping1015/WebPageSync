
from database import Base
db =
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    phone = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    isenable = Column(BOOLEAN)
    adddate = Column(DATETIME)
    md5code = Column(String(40), unique=True)

    def __init__(self, username=None, password=None, phone=None, email=None, isenable=None, adddate=None, md5code=None):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.isenable = isenable
        self.adddate = adddate
        self.md5code = md5code

class FavoriteList(Base):
    __tablename__ = 'favoritelist'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    isdefault = Column(SmallInteger)
    adddate = Column(DATETIME)
    userid = Column(Integer)

    def __init__(self, username=None, password=None, phone=None, email=None, isenable=None, adddate=None, md5code=None):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.isenable = isenable
        self.adddate = adddate
        self.md5code = md5code