from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    last_name = models.CharField('Last Name', max_length=40, blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
