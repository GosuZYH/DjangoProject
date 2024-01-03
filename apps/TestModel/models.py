from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'user'
    name = models.CharField(max_length=255, primary_key=True)
    sex = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name} sex:{self.sex} age:{self.age}"

    def __repr__(self):
        return f"Name:{self.name} sex:{self.sex} age:{self.age}"
