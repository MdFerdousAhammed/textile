from django.shortcuts import render,redirect
from beximapp.models import Post,Postai

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


 

def home(request):
    return render(request,"home.html")
def admin(request):
    return render(request,"admin.html")
def help(request):
    return render(request,"help.html")
def contact(request):
    return render(request,"contact.html")

    





def  post(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        details = request.POST.get("details")
        image = request.FILES.get("image")
        obj = Post(name = username,email = email,details = details,image= image)
        obj.save()
        return redirect('post')
        
    return render(request,"from.html")

def postview(request):
    post = Post.objects.all()
    return render(request,"post.html",{"post" : post})



    # api
def create_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        image = request.FILES.get('image')

        posts = Postai(image=image, title=title, name=name)
        posts.save()

        return redirect('postai')

    return render(request, 'ai.html')



def postai(request):
    post = Postai.objects.all()
    return render(request,"postai.html",{"post":post})



# post views all image and emoloier 
# create a post html tempalte

    
# def handler404(request, exception):
#     return render(request, 'earro.html', status=404)


    






def authlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('aifrom') # replace with your desired success URL
        

            


            
    else:
        form = AuthenticationForm()  
    return render(request, 'login.html', {'form': form})



# def login(request):
#     if request.method =="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username,password = password)
#         if user is not None:
#             login(request,user)
#             return redirect('aifrom')

#         else:
#             print("invalid user name")

#     return render(request,"login.html")
    

