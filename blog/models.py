from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # __str__ shows the Title of each Blog Post on /admin/blog
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:240]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')