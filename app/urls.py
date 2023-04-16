from django.urls import path
from .views import show_profiles, add_profile, sign_in, sign_up, edit_profile, change_password

urlpatterns = [

    path('', show_profiles, name='profiles'),
    path('add_profile', add_profile, name='form'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),

]
