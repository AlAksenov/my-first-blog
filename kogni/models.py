from django.db import models

# Create your models here.
class scenariy (models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='kogni_images', blank=True)
    file = models.FileField(upload_to='kogni_karti' , blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
        #return self.title +'  ||  '+ self.description


class Node_men(models.Model):
    id_node = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.FloatField()


    def __str__(self):
        return self.name

class Node_mar(models.Model):
    id_node = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.FloatField()


    def __str__(self):
        return self.name

class Node_log(models.Model):
    id_node = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.FloatField()


    def __str__(self):
        return self.name