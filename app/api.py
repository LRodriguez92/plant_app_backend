# from rest_framework import generics, permissions, mixins
# from rest_framework.response import Response
# from .serializers import RegisterSerializer, UserSerializer
# from django.contrib.auth.models import User


# # Register API
# class RegisterApi(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args,  **kwargs):
#         print("REQUEST DATA:")
#         print(request.data)
#         serializer = self.get_serializer(data=request.data)
#         print("SERIALIZER:")
#         print(serializer)
#         serializer.is_valid()
#         user = serializer.save()
#         print('USER:')
#         print(user)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })
