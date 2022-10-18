from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
# Import Booking model from models
from .models import Teetime


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "custom-red",
            }
        )


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_active": "custom-red",
            }
        )
