# webstudy/middleware.py

class XFrameOptionsRemoveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Only remove the header for media files
        if request.path.startswith('/media/'):
            if 'X-Frame-Options' in response:
                del response['X-Frame-Options']
        return response