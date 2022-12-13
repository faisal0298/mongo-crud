from fastapi import FastAPI,Response
from mongoengine import connect
from models import User,Role,Project
from serializer import createuser,updateuser,createproject
import json
from fastapi_socketio import SocketManager
import socketio
# from helpers import SocketManager,get_role
from helpers import get_role,get_email
from fastapi.middleware.cors import CORSMiddleware
import datetime


app = FastAPI()
sio = SocketManager(app=app)

connect(db="mongotest", host="localhost",port=27017)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )



# @app.sio.on('join')
# async def handle_join(sid, *args, **kwargs):
#     await sio._sio.emit('lobby', 'User joined')


# @sio.on('test')
# async def test(sid, *args, **kwargs):
#     print(sid)
#     await sio._sio.emit('hey', 'joe',room=sid)


# @sio.on('alluser')
# async def data(sid, *args, **kwargs):
#     user= User.objects().to_json()
#     data=json.loads(user)
#     await sio._sio.emit('data',list(data))


# @sio.on("find")
# async def finduser(sid,*args,**kwargs):
#     print(args)
#     # user=User.objects.get(email=email)
#     # print(user.payload())
#     await sio._sio.emit('data',"success")


@app.on_event("startup")
def add_role():
    if not Role.objects().count()>=5: 
        print(Role.objects())
        role=[Role(role_name="superadmin"),
                Role(role_name="masteradmin"),
                Role(role_name="admin"),
                Role(role_name="member"),
                Role(role_name="user")
                ]
        Role.objects.insert(role)
        return 


# @app.get("/roles")
# def all_roles():
#     roles= Role.objects().to_json()
#     data=json.loads(roles)
#     return data


@app.get("/roles")
def all_roles():
    roledata=[]
    userrole=[]
    
    roles= Role.objects()

    for name in roles:
        roledata.append(name.role_name)
        userrole.append(User.objects(rolename=name).count())

    return {"role_name":roledata,
    "role count" : userrole}


@app.get("/fetch_role")
def get_role_list(role:str):
    roleName = get_role(role)
    role = User.objects(rolename=roleName).to_json()

    print(role)
    return json.loads(role)


@app.get("/alluserlist")
def all_users():
    user= User.objects.to_json()
    data=json.loads(user)
    return data


@app.get("/")
def all_users():
    user= User.objects().count()
    projects = Project.objects().count()
    data = Project.objects()

    last=User.objects(created_at__gte=("2022-10-01"),created_at__lt=("2022-11-01")).count()
    current=User.objects(created_at__gte=("2022-11-01"),created_at__lte=datetime.datetime.utcnow().__str__()).count()
    print(datetime.datetime.utcnow().__str__())
    percentage= (current - last)/ current * 100.0

    print(last)
    print(current)
    print(round(percentage,2))

    sum = data.sum("Annotationcount")  #below for loop does the same work
    # sum=0
    # for annotate in data:
    #     annotatedata = annotate.Annotationcount
    #     sum+=annotatedata
    return [
        {"name":"Total Users Registered","count":user,"text":"since last month"},
        {"name":"Total Models Build","count":projects,"text":"since last month"},
        {"name": "Total Data Annotated","count":sum,"text": "Since last month"}]
    
    
@app.get("/fetch_user")
def get_user(email:str,response:Response):
    user= User.objects.get(email=email)
    # if not user:
    #     response.status_code=404
    #     return "not found"
    return user.payload()
    # return "not found"


@app.post("/add_user")
def add_user(userInput:createuser):
    roleName = get_role(userInput.rolename)
    new_user = User(fullname=userInput.fullname,age=userInput.age,phone=userInput.phone,
                    address=userInput.address,email=userInput.email,rolename=roleName)
    
    new_user.save()
    data= json.loads((new_user).to_json())
    return data


@app.post("/add_project")
def add_project(Input:createproject):
    Email = get_email(Input.email)
    new_project = Project(email=Email,name=Input.name,Annotationcount=Input.Annotationcount)
    new_project.save()
    data= json.loads((new_project).to_json())
    return data


@app.put("/update_user")
def update_user(user:updateuser):
    update_user = User.objects(email=user.email).first()
    update_user.update(set__fullname=user.name,set__age=user.age)
    return "success"


@app.delete("/delete_user")
def remove_user(email:str):
    user=User.objects.get(email=email)
    user.delete()
    return "deleted successfully"
