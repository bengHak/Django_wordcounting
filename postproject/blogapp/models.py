from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.CharField(("Title"), max_length=100)
    published_date = models.DateField(("Date published"), auto_now=False, auto_now_add=False)
    body = models.TextField(("Body"))

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 
