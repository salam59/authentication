from rest_framework_simplejwt.tokens import RefreshToken

class UserTypeMiddleWare:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        user_type = None
        auth_header = request.META.get('HTTP_AUTHORIZATION', '').split()
        if len(auth_header) == 2 and auth_header[0].lower() == 'bearer':
            try:
                token = auth_header[1]
                decoded_token = RefreshToken(token)
                user_type = decoded_token.payload.get('user_type')
            except Exception:
                pass

        request.user_type = user_type
        response = self.get_response(request)
        return response