from django.db import models
from authorization.models import Users

class Personaldict(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        db_table = 'PersonalDict'


class Words(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255, db_collation='Ukrainian_CI_AS')
    translation = models.CharField(max_length=255, db_collation='Ukrainian_CI_AS')

    class Meta:
        db_table = 'Words'


class Wordsindict(models.Model):
    dict = models.OneToOneField(Personaldict, models.DO_NOTHING, primary_key=True)
    word = models.ForeignKey(Words, models.DO_NOTHING)

    class Meta:
        db_table = 'WordsInDict'
