from django.db import models
from django.utils import timezone 

# Create your models here.

class Post(models.Model):
    '''
    Esta clase representa las entradas al blog. 
    '''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank = True, null= True)


    def publish(self):
        self.published_date = timezone.now
        self.save()


    def __str__(self):
        return self.title
