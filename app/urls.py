from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path(
        'web_teetime/',
        views.WebTeetimeView.as_view(),
        name='web_teetime'
    ),
    path(
        'create_account/',
        views.CreateAccount.as_view(),
        name='create_account'
    ),
    path(
        'edit_account/<str:user>/',
        views.EditAccount.as_view(),
        name='edit_account'
    ),
    path(
        'change_teetime/',
        views.ChangeTeetime.as_view(),
        name='change_teetime'
    ),
    path(
        'edit_teetime/<str:teetime_id>/',
        views.EditTeetime.as_view(),
        name='edit_teetime'
    ),
    path(
        'delete_teetime/<str:teetime_id>/',
        views.DeleteTeetime.as_view(),
        name='delete_teetime'
    ),
]
