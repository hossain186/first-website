from django.db import models

# Create your models here.
class Topic(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Artical(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    artical = models.TextField(null=True , blank=True)

    create = models.DateTimeField(auto_now= True)
    update = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-create' , '-update']


    

    def __str__(self):
        return self.artical

