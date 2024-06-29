from django.db import models

# Create your models here.

class Categoris(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Post(models.Model):
    publisher = models.CharField(max_length=470)
    p_date = models.DateTimeField(null=True)
    c_view = models.IntegerField(default=0)
    title = models.CharField(max_length=70,default="Null")
    status = models.BooleanField(default=True)
    disc = models.TextField()
    image = models.ImageField(upload_to='blog',default='blog/1571774856481.jpg')
    category = models.ManyToManyField(Categoris, blank=True)
    def __str__(self):
        return f"{self.id}.{self.title}"
    
class Comment(models.Model):
    about = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    uname = models.CharField(max_length=255)
    date_modified = models.DateTimeField(auto_created=True)
    comment = models.TextField()
    def __str__(self):
        return f"{self.id} - {self.uname} - {self.about}"
    
