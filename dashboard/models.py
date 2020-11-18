from django.db import models

# Create your models here.
class Home(models.Model):
    # Adding status tuple to the backend
    STATUS= (
        ('Open', 'Open'),
        ('Pending', 'Pending'),
        ('Work in Progress','Work in Progress'),
        ('Closed','Closed'),
        )
    name          = models.CharField(max_length=30)
    email         = models.EmailField()
    phone         = models.CharField(max_length=14)
    issuetype     = models.CharField(max_length=40, default='Blank/Frozen Screen')
    status        = models.CharField(max_length=40,default='Open',choices=STATUS)
    desc          = models.TextField()
    
    def __str__(self):
        return self.name+" "+self.issuetype