# Controllers

from ninja_extra import api_controller, route


@api_controller(
    '/biomes',
    tags=['Rota - Biomas'],
    auth=None
)

class BiomesController:
    
    @route.get('')
    def list(self, request):
        """
        List all biomes
        """
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
        return 'delete'