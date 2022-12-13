from mongoengine import Document,StringField,IntField,DateTimeField,EmailField
from mongoengine import ReferenceField,BooleanField
import datetime


class Role(Document):
    role_name = StringField(max_length=100)
    created_at = DateTimeField(default=datetime.datetime.utcnow())


class User(Document):
    rolename = ReferenceField("Role")
    fullname = StringField(max_length=200)
    age = IntField()
    phone = IntField()
    address = StringField(max_length=250)
    email = EmailField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    is_active = BooleanField(default=True)

  
    def payload(self):
        return {
            "fullname": self.fullname,
            "age": self.age,
            "phone" : self.phone,
            "address" : self.address,
            "email": self.email,
            "created_at":self.created_at,
            "is_active" : self.is_active,
            "role" : self.rolename
        }


class Project(Document):
    email = ReferenceField("User")
    name = StringField(max_length=200)
    Annotationcount = IntField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())