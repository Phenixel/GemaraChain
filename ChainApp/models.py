from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")


class Session(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_limit = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.date_limit < timezone.now().date():
            raise ValidationError(_("The date limit must be a future date."))

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")
        ordering = ['-created_at']


class Gemarot(models.Model):
    name = models.CharField(max_length=255)
    livre = models.CharField(max_length=255)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Gemarot")
        verbose_name_plural = _("Gemarot")


class Gemara(models.Model):
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    chosen_by = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)
    choose_gemarot = models.ForeignKey('Gemarot', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.choose_gemarot} - Session: {self.session.name}"

    class Meta:
        verbose_name = _("Gemara")
        verbose_name_plural = _("Gemarot")
