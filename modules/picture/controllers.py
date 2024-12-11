# Controllers

from ninja_extra import api_controller, route


@api_controller(
    '/picture',
    tags=['Rota - Picture'],
    auth=None
)

class PictureController:
    
    @route.get('', )
    def list(self, request):
        return 'list'
    
    @route.get('/{id}', )
    def get(self, request, id: int):
        return 'get'
    
    @route.post('', )
    def post(self, request):
        return 'post'
    
    @route.put('/{id}', )
    def put(self, request, id: int):
        return 'put'
    
    @route.delete('/{id}', )
    def delete(self, request, id: int):
        return