from django.db import models
from registration.signals import user_registered
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
# Si hay problemas con null constraint, quitar campos del modelo que no han sido anadidos


class Place(models.Model):
    pattern = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no-avatar.png')
    birth_date = models.DateField(default=datetime.now)
    GENDER = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER, default='M')
    phone = models.IntegerField(null=True, blank=True)
    biography = models.TextField(blank=True)  # opcional
    location = models.ForeignKey(Place, default="")

    def __str__(self):
        return self.gender

    def user_registered_callback(sender, user, request, **kwargs):
        profile = Profile(user=user)
        #profile.location = get_object_or_404(Place, name=request.POST["location"])
        profile.save(commit=False)

    user_registered.connect(user_registered_callback)
