from django.urls import path
from .views import go_to_home_page

urlpatterns = [
    path('home/', go_to_home_page, name='home'),
]
