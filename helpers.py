# import socketio
from typing import Union
from fastapi import FastAPI
from models import Role,User


# class SocketManager:
#     def __init__(
#         self,
#         app: FastAPI,
#         mount_location: str = "/ws",
#         socketio_path: str = "socket.io",
#         cors_allowed_origins: Union[str, list] = '*',
#         async_mode: str = "asgi",
#         **kwargs
#     ) -> None:
#         self._sio = socketio.AsyncServer(async_mode=async_mode, cors_allowed_origins=cors_allowed_origins, **kwargs)
#         self._app = socketio.ASGIApp(
#             socketio_server=self._sio, socketio_path=socketio_path
#         )

#         app.mount(mount_location, self._app)
#         app.sio = self._sio

#     def is_asyncio_based(self) -> bool:
#         return True

#     @property
#     def on(self):
#         return self._sio.on
    

def get_role(role_name):
    return Role.objects.get(role_name=role_name)

def get_email(email):
    return User.objects.get(email=email)

