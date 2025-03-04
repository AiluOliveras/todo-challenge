import logging

logger = logging.getLogger('django')

class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #Registra endpoints accedidos
        logger.info(f'Accediendo al endpoint: {request.path}')
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        #Registra errores
        logger.error(f'Error en {request.path}: {exception}')