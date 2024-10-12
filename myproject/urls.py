from django.contrib import admin
from django.urls import path
# from home.views import
from recipe.views import recipe,delete_recipe,update_recipe,loginPage, aboutPage, contactPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('about/', aboutPage, name='aboutPage'),
    path('contact/', contactPage, name='contact'),
    path('recipe/', recipe, name='recipe'),
    path('delete_recipe/<id>/',delete_recipe,name='delete_recipe' ),
    path('update_recipe/<id>/', update_recipe, name='update_recipe'),
    path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Append media URL patterns
