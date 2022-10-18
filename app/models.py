import uuid
from django.db import models
from django.contrib.auth.models import User
STATUS = ((0, "Teetime Requested"), (1, "Teetime Accepted"))

class Teetime(models.Model):
    teetime_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_teetime")
    teetime_date = models.DateField(auto_now=False)
    teetime_time = models.TimeField(auto_now=False)
    teetime_comments = models.TextField(max_length=180, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    player_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-teetime_date']
class UserAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return str(self.user)