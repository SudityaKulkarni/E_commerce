from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer ,UserCreateSerializer ,UserUpdateSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

#this is class based views for getting all users and creating users
class UserListCreateView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializer(users, many = True)

        if not users:
            return Response({"messgae": "No users found"}, status = status.HTTP_404_NOT_FOUND)
        
        return Response(serializers.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserCreateSerializer(data = request.data)      #takes in the json data sent from the frontend

        if serializer.is_valid():                                   #checks if the input format is valid or not
            serializer.save()                                       #saves data into the database
            return Response(serializer.data, status = status.HTTP_201_CREATED)  #returns response with the data and status code 201
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) #returns error if the input format is not valid
    

#this is class based views for getting a single user and updating ,deleting a user
class UserDetailView(APIView):
        def get(self, request ,id):
            user = get_object_or_404(User, id = id)
            serializer = UserSerializer(user)   
            if not user:
                return Response({"message": "User not found"}, status = status.HTTP_404_NOT_FOUND)
            
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        def put(self, request, id):
            user = get_object_or_404(User, id = id)
            serializer = UserUpdateSerializer(user, data = request.data, partial = True)    #partial = True allows partial update of the user data  
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


        def delete(self, request, id):
            user = get_object_or_404(User, id = id)
            # user = User.objects.get(id = id)  #alternative way to get the user object
            if not user:
                return Response({"message": "User not found"}, status = status.HTTP_404_NOT_FOUND)
            
            user.delete()
            return Response({"message": "User deleted successfully"}, status = status.HTTP_204_NO_CONTENT)