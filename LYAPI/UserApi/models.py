# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CxxUser(models.Model):
    uid = models.AutoField(primary_key=True)
    u_account = models.CharField(max_length=20)
    u_name = models.CharField(max_length=50, blank=True, null=True)
    u_passwd = models.CharField(max_length=40, blank=True, null=True)
    u_phone = models.CharField(max_length=20)
    u_sex = models.CharField(max_length=5, blank=True, null=True)
    u_address = models.CharField(max_length=100, blank=True, null=True)
    u_token = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cxx_user'

