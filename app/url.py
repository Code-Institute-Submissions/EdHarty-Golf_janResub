from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
]
    

