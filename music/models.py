from django.db import models

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Singer(models.Model):
    id = models.AutoField(primary_key=True) 
    content = models.TextField(blank=True)
    debut = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
    release = models.DateField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)