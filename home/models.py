# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Avaliacao(models.Model):

    #__Avaliacao_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    descricao = models.TextField(max_length=255, null=True, blank=True)

    #__Avaliacao_FIELDS__END

    class Meta:
        verbose_name        = _("Avaliacao")
        verbose_name_plural = _("Avaliacao")


class Parametroitem(models.Model):

    #__Parametroitem_FIELDS__
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    questao = models.IntegerField(null=True, blank=True)
    a = models.IntegerField(null=True, blank=True)
    b = models.IntegerField(null=True, blank=True)
    c = models.IntegerField(null=True, blank=True)

    #__Parametroitem_FIELDS__END

    class Meta:
        verbose_name        = _("Parametroitem")
        verbose_name_plural = _("Parametroitem")


class Uploadrespostas(models.Model):

    #__Uploadrespostas_FIELDS__
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    arquivo = models.CharField(max_length=255, null=True, blank=True)
    data_upload = models.DateTimeField(blank=True, null=True, default=timezone.now)
    processado = models.BooleanField()

    #__Uploadrespostas_FIELDS__END

    class Meta:
        verbose_name        = _("Uploadrespostas")
        verbose_name_plural = _("Uploadrespostas")



#__MODELS__END
