from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, db_collation='Ukrainian_CI_AS')
    password = models.CharField(max_length=255, db_collation='Ukrainian_CI_AS')
    name = models.CharField(max_length=255, db_collation='Ukrainian_CI_AS')

    class Meta:
        db_table = 'Users'

