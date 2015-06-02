from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    """
    It represents a record of any student
    """
    student = models.ForeignKey(User)
    book = models.CharField(max_length=100)
    marked_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    read_from = models.DateField()
    read_until = models.DateField()
    
    def __unicode__(self):
        return "%s  READ -->>  %s" % (self.student.username, self.book)
    
    
class School(models.Model):
    """
    It represents a school. 
    It's not related yet, no required.
    """
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)