from django.shortcuts import render,redirect
# Create your views here.
from recipe.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desciption = data.get('recipe_desciption')
        recipe_image = request.FILES.get('recipe_image')

        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desciption=recipe_desciption,  # Corrected here
            recipe_image=recipe_image
        )
    data = Recipe.objects.all()

    if request.GET.get('search_val'):
        data = data.filter(recipe_name__icontains = request.GET.get('search_val'))
    return render(request,'recipe.html',context={'data':data})

def delete_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('/recipe/')

def update_recipe(request,id):
    updating_recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_desciption = request.POST.get('recipe_desciption')
        recipe_image = request.FILES.get('recipe_image')

        # Save the updated object to the database
        if recipe_image:
            updating_recipe.recipe_image = recipe_image

        updating_recipe.recipe_name = recipe_name
        updating_recipe.recipe_desciption = recipe_desciption
        updating_recipe.recipe_image = updating_recipe.recipe_image
        updating_recipe.save()
        # Redirect or return a response
        return redirect('/recipe/')

    return render(request, 'updateRecipe.html', context={'data': updating_recipe})





def loginPage(request):
    title = 'Home Page'
    if request.method=='POST':
        data = request.POST
        username = data.get("username")    
        password = data.get("password")
        
        data = Recipe.objects.all()
        user = authenticate(request, username=username, password=password)
        print("user",username,password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            # context = Recipe.objects.all()
            return redirect('/recipe/')
        else:
            # Optionally, you can add a message for invalid login
            error_message = "Invalid username or password."
            return render(request, 'login.html', context={'title': title, 'error_message': error_message})
    return render(request,'login.html',context={'title':title})


def createUser(request):
    try:
        if request.method == 'POST':
            data = request.POST
            username = data.get("username")    
            password = data.get("password")
            email = data.get("email")
            first_name = data.get("first_name")
            last_name = data.get("last_name")  # Fixed key for last name
            
            # Create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Redirect to the login page or another page after successful registration
            return redirect('loginPage')  # Change 'login' to your actual login URL name

        return render(request, 'createUser.html')
    
    except Exception as ex:
        print(ex)
        # Optionally, you could handle the error and provide feedback to the user
        return render(request, 'createUser.html', {'error_message': 'Error creating user. Please try again.'})

def aboutPage(request):
    title = 'About Page'
    return render(request,'about.html',context={'title':title})

def contactPage(request):
    locations = {
        'New_York': 'New York',
        'Los_Angeles': 'Los Angeles',
        'Chicago': 'Chicago',
        'Houston': 'Houston',
        'Miami': 'Miami'
    }
    title = 'Contact Page'
    return render(request,'contact.html',context={'title':title,'locations':locations})

