from django.shortcuts import render
# Create your views here.
from recipe.models import *

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
    data = Recipe.objects.all()
    return render(request, 'recipe.html', context={'data': data})

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
        data = Recipe.objects.all()
        return render(request, 'recipe.html', context={'data': data})

    return render(request, 'updateRecipe.html', context={'data': updating_recipe})





def loginPage(request):
    title = 'Home Page'
    return render(request,'index.html',context={'title':title})

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

