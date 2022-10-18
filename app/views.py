from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
# Import Booking model from models
from .models import Teetime, UserAccount
from .forms import UpdateBookingDetails, EditAccountForm


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "computer-blue",
            }
        )


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_active": "computer-blue",
            }
        )


class CreateAccount(View):
    template_name = "create_account.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_account.html",
        )

    def post(self, request):
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        tele = request.POST.get("phone_number")

        CreateUserAccount = UserAccount.objects.create(
            first_name=f_name,
            last_name=l_name,
            phone_number=tele,
            user=request.user,
        )

        CreateUserAccount.save()

        return redirect(reverse('home'))


class EditAccount(View):
    model = UserAccount
    template_name = "edit_account.html"
    context_object_name = 'edit_account'

    def get(self, request, user, *args, **kwargs):
        account = UserAccount.objects.filter(user=user).first()
        if rofile is None:
            return redirect(reverse('create_account'))

        return render(
            request,
            "edit_account.html",
            {
                "account": account,
                "updated": False,
                "Edit_AcccountForm": EditAccountForm,
                "edit_account_active": "computer-blue",
            },
        )

    def post(self, request, user, *args, **kwargs):
        account = UserAccount.objects.get(user=user)

        edit_account_form = EditAccountForm(request.POST, instance=account)

        if edit_account_form.is_valid():
            account_updates = edit_account_form.save()
        else:
            edit_account_form = EditAccountForm(instance=account)

        return render(
            request,
            "edit_account.html",
            {
                "account": account,
                'updated': True,
                "Edit_AccountForm": edit_account_form,
            },
        )


class ChangeBooking(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "change_booking.html"
    paginate_by = 6
    extra_context = {
        "change_booking_active": "computer-blue"
    }

    def get_queryset(self):
        return Booking.objects.filter(user_id=self.request.user)


class WebBookingView(View):
    template_name = "web_booking.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "web_booking.html",
            {
                "web_booking_active": "computer-blue",
            }
        )

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        guest_count = request.POST.get("guest_count")
        comments = request.POST.get("comments")

        web_booking = Booking.objects.create(
            booking_date=date,
            booking_time=time,
            guest_count=guest_count,
            user=request.user,
            booking_comments=comments
        )

        web_booking.save()

        return redirect(reverse('_booking'))


class EditBooking(View):
    model = Booking
    template_name = "edit_booking.html"
    context_object_name = 'edit_booking'

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                "updated": False,
                "Update_BookingDetails": UpdateBookingDetails(instance=booking)
            },
        )

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, pk=booking_id)

        booking_details_form = UpdateBookingDetails(
            request.POST, instance=booking)

        if booking_details_form.is_valid():
            booking.status = 0
            booking_updates = booking_details_form.save()
        else:
            booking_details_form = UpdateBookingDetails(instance=booking)

        return render(
            request,
            "edit_booking.html",
            {
                "booking": booking,
                'updated': True,
                "Update_BookingDetails": booking_details_form,
            },
        )


class DeleteBooking(DeleteView):
    model = Teetime
    pk_url_kwarg = "teetime_id"
    success_url = reverse_lazy("change_booking")
    template_name = "delete_booking.html"
