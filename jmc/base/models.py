# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.db import models

# Inrootz Stuff
from account.models import UserProfile


class TimeAuditModel(models.Model):

    """ To track when the record was created and last modified """
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="Created At",)
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="Last Updated At")

    class Meta:
        abstract = True


class UserAuditModel(models.Model):

    """ To track who created and last modified the record """
    created_by = models.ForeignKey(UserProfile, related_name='created_%(class)s_set+',
                                   null=True, blank=True, verbose_name="Created By")
    updated_by = models.ForeignKey(UserProfile, related_name='updated_%(class)s_set+',
                                   null=True, blank=True, verbose_name="Updated By")

    class Meta:
        abstract = True


class CreatedTimeUserAuditModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At",)
    created_by = models.ForeignKey(UserProfile, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name="Created By")


class AuditModel(TimeAuditModel, UserAuditModel):

    class Meta:
        abstract = True
