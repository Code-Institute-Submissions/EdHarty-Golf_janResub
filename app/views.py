from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Django generic libary
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
# Import Teetime
from .models import Teetime, UserAccount
from .forms import UpdateTeetimeDetails, EditAccountForm


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active",
            }
        )


class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_active",
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
        if account is None:
            return redirect(reverse('create_account'))

        return render(
            request,
            "edit_account.html",
            {
                "account": account,
                "updated": False,
                "Edit_AcccountForm": EditAccountForm,
                "edit_account_active"
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


class ChangeTeetime(generic.ListView):
    model = Teetime
    queryset = Teetime.objects.all()
    template_name = "change_teetime.html"
    paginate_by = 6
    extra_context = {
        "change_teetime_active"
    }

    def get_queryset(self):
        return Teetime.objects.filter(user_id=self.request.user)


class WebTeetimeView(View):
    template_name = "web_teetime.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "web_teetime.html",
            {
                "web_teetime_active"
            }
        )

    def post(self, request):
        date = request.POST.get("date")
        time = request.POST.get("time")
        player_count = request.POST.get("player_count")
        comments = request.POST.get("comments")

        web_teetime = Teetime.objects.create(
            teetime_date=date,
            teetime_time=time,
            player_count=player_count,
            user=request.user,
            teetime_comments=comments
        )

        web_teetime.save()

        return redirect(reverse('change_teetime'))


class EditTeetime(View):
    model = Teetime
    template_name = "edit_teetime.html"
    context_object_name = 'edit_teetime'

    def get(self, request, teetime_id, *args, **kwargs):
        teetime = get_object_or_404(teetime, pk=teetime_id)

        return render(
            request,
            "edit_teetime.html",
            {
                "teetime": teetime,
                "updated": False,
                "Update_TeetimeDetails": UpdateTeetimeDetails(instance=teetime)
            },
        )

    def post(self, request, teetime_id, *args, **kwargs):
        teetime = get_object_or_404(Teetime, pk=teetime_id)

        teetime_details_form = UpdateTeetimeDetails(
            request.POST, instance=teetime)

        if teetime_details_form.is_valid():
            teetime.status = 0
            teetime_updates = teetime_details_form.save()
        else:
            teetime_details_form = UpdateTeetimeDetails(instance=teetime)

        return render(
            request,
            "edit_teetime.html",
            {
                "teetime": teetime,
                'updated': True,
                "Update_TeetimeDetails": teetime_details_form,
            },
        )


class DeleteTeetime(DeleteView):
    model = Teetime
    pk_url_kwarg = "teetime_id"
    success_url = reverse_lazy("change_teetime")
    template_name = "delete_teetime.html"
