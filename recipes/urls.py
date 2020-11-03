from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homepage import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('newrecipe/', views.recipe_form_view, name="newrecipe"),
    path('newcategory/', views.category_form_view, name="newcategory"),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('signup/', views.signup_view, name="signupview"),
    path('recipe/<int:id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:id>/remove/', views.remove_recipe, name='remove_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe, name="recipe"),
    path('category/<int:id>/remove/', views.remove_category, name='remove_category'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
