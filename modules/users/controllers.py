from modules.users.models import User
from ninja_extra import api_controller, route
from modules.users.services import Services
from modules.users.schemas import UserListSchema, UserPostSchema, UserPutSchema, ErrorResponse
from typing import List
from ninja import Form, File, UploadedFile


@api_controller(
    '/users',
    tags=['Rota de Usuários'],
)

class UsersController:
    
    services = Services
    
    @route.get('', response={200: List[UserListSchema]})
    def list(self, request):
        return self.services.list()
    
    @route.get('/{id}', response={200: UserListSchema})
    def get(self, request, id: int):
        return self.services.get(id=id)
    
    @route.post('', response={201: UserListSchema, 500: ErrorResponse})
    def post(self, request, payload: UserPostSchema = Form(...), profile_picture: UploadedFile = File(None)):
        
        return self.services.post(payload=payload.dict(), file=profile_picture)
    
    @route.put('/{id}', response={200: UserListSchema, 500: ErrorResponse})
    def put(self, request, id: int, payload: UserPutSchema = Form(...), profile_picture: UploadedFile = File(None)):
        
        payload_dict = payload.dict(exclude_unset=True)
        
        if profile_picture:
            payload_dict['profile_picture'] = profile_picture
        
        status_code, result = self.services.put(id=id, payload=payload_dict, file=profile_picture)
        
        return result
        
        
    
    @route.delete('/{id}', response={204: None})
    def delete(self, request, id: int):
        return self.services.delete(id=id)
    