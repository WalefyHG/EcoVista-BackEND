# Controllers
from ninja_extra import api_controller, route



@api_controller(
    '/reporting',
    tags=['Rota - Denuncias'],
    auth=None
)
class ReportingController:
    
    @route.get('/{id}')
    def get_report(self, request, id: int):
        return {'id': id, 'name': 'Report'}
    
    @route.post('/')
    def post_report(self, request):
        return {'name': 'Report'}
    
    @route.put('/{id}')
    def put_report(self, request, id: int):
        return {'id': id, 'name': 'Report'}
    
    @route.delete('/{id}')
    def delete_report(self, request, id: int):
        return {'id': id, 'name': 'Report'}
    