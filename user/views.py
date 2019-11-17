from django.shortcuts import render, redirect
from .form import MyUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(
            request.POST)

        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get("username")
            messages.success(request,f"User registration Success with name of {username}")
            return redirect("product-home")
      
    form = MyUserCreationForm()
    return render(request,"user/register.html",{"form":form}) 


    #     else : 
    #         form = UserCreationForm()
    #         return render(request, "user/register.html", {"form": form})
    # else : 
    #     form = UserCreationForm()
    #     return render(request,"user/register.html",{"form":form})
