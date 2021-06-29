from django.shortcuts import render
import pyrebase 
from django.contrib import auth

firebaseConfig = {
    "apiKey": "AIzaSyCpbsf3iwViEyly4rtxAF-rLwslpHar8y4",
    "authDomain": "djangostudy-64f2f.firebaseapp.com",
    "projectId": "djangostudy-64f2f",
    "storageBucket": "djangostudy-64f2f.appspot.com",
    "messagingSenderId": "732727150916",
    "appId":  "1:732727150916:web:96f2ea812ca03d210aaf11",
    "measurementId": "G-73SJSBKYJ6",
    "databaseURL": "https://djangostudy-64f2f-default-rtdb.firebaseio.com"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database=firebase.database()


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def signin(request):
    return render(request, "blog/signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = 'invalid cerediantials'
        return render(request,'blog/signIn.html',{'msg':message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, 'blog/postsign.html',{'e':email})

def register(request):
    return render(request,'blog/register.html')


def postregister(request): 
    username=request.POST.get('username')
    firstname=request.POST.get('first')
    lastname=request.POST.get('last')
    email=request.POST.get("email")
    passw=request.POST.get("pass")
    repassw=request.POST.get("repass")
    # if not(repassw==passw):
    #     message="Re enter confirm password"
    #     return render(request,"blog/register.html",{"messg":message})
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"username":username,"firstname":firstname,"lastname":lastname,"status":"1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"blog/register.html",{"msg":message})
    
    return render(request,"blog/signIn.html",{"username":username,"password":passw})


def logout(request):
    auth.logout(request)
    return render(request,'blog/home.html')