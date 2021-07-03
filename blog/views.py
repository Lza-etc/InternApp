from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib import auth
from blog.models import Users
from django.http import JsonResponse

from rest_framework.response import Response
from blog.firebase_client import FirebaseClient
from blog.serializers import UserSerializer
from rest_framework import status
# import django_filters.rest_framework import DjangoFilterBackend



class UserListAV(APIView):
    client=FirebaseClient()
    
    def get(self, request, format=None):
        user=self.client.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        print("HELLODIRECT",request.data)
        serializer=UserSerializer(data=request.data)
        print("HELLODIRECT",serializer)
        serializer.is_valid(raise_exception=True)
        print("HELLODIRECT")
        self.client.create(serializer.data)
        print("HELLODIRECT",serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class UserDetailsAV(APIView):

    client=FirebaseClient()

    def get(self, request,pk):
        try:
            user=self.client.get_by_id(pk)
        except Users.DoesNotExist:
            return Response({"Error":"User not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(user)
        return Response(serializer.data)

#     def put(self,request,pk):
#         user=Users.objects.get(pk=pk)
#         serializer=UserSerializer(user,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         users=Users.objects.get(pk=pk)
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    # def retrieve(self, request, pk=None):
    #     todo = self.client.get_by_id(pk)

    #     if todo:
    #         serializer = TodoSerializer(todo)
    #         return Response(serializer.data)

    #     raise NotFound(detail="Todo Not Found", code=404)

    # def destroy(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     self.client.delete_by_id(pk)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     serializer = TodoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     self.client.update(pk, serializer.data)

    #     return Response(serializer.data)

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def signin(request):
    return render(request, "blog/signIn.html")

def postsign(request):
    print(request)
    username=request.POST.get('username')
    passw = request.POST.get('pass')

    print(username,passw)
    # try:
    #     user = authe.sign_in_with_email_and_password(email,passw)
    # except:
    #     message = 'invalid cerediantials'
    #     return render(request,'blog/signIn.html',{'msg':message})
    # return render(request, 'blog/postsign.html',{'e':request.POST})

def register(request):
    return render(request,'blog/register.html')


def postregister(request): 
    username=request.POST.get('username')
    firstname=request.POST.get('first')
    lastname=request.POST.get('last')
    email=request.POST.get("email")
    passw=request.POST.get("pass")
    repassw=request.POST.get("repass")

    if not(passw==repassw):
        message="Confirm Password Again"
        return render(request,"blog/register.html",{"msg":message})
   
    try:
    
        client=FirebaseClient()
        data={"username":username,"firstname":firstname,"lastname":lastname,"email":email }

        serializer=UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        client.create(serializer.data)
    except:
        message="Unable to create user"
        return render(request,"blog/register.html",{"msg":message})
    
    return render(request,"blog/signIn.html",{"username":username})


# def logout(request):
#     # del request.session['uid']
#     # auth.logout(request)   
#     return render(request,'blog/home.html')