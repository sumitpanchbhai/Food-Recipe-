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
    return render(request,'recipe.html',context={'data':data})

def delete_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    data = Recipe.objects.all()
    return render(request, 'recipe.html', context={'data': data})

