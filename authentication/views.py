from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginRequest(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        token_response = super().post(request, *args, **kwargs)
        
        # Assuming token_response is a Response object
        token_data = token_response.data
        # Set session cookie
        request.session['token'] = token_data['access']
        # Combine the responses as needed
        combined_data = {
            'token': token_data,
        }
        
        return JsonResponse(combined_data)

