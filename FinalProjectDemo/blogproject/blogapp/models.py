from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('authorapp.Author', on_delete=models.CASCADE)
    category = models.ForeignKey('categoryapp.Category', on_delete=models.CASCADE)