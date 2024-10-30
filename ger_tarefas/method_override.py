class MethodOverrideMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and '_method' in request.POST:
            request.method = request.POST['_method'].upper()
        return self.get_response(request)