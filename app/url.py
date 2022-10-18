from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path(
        'web_booking/',
        views.WebBookingView.as_view(),
        name='web_booking'
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
        'change_booking/',
        views.ChangeBooking.as_view(),
        name='change_booking'
    ),
    path(
        'edit_booking/<str:booking_id>/',
        views.EditBooking.as_view(),
        name='edit_booking'
    ),
    path(
        'delete_booking/<str:booking_id>/',
        views.DeleteBooking.as_view(),
        name='delete_booking'
    ),
]