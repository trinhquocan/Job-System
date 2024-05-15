from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(BaseModel):
    subject = models.CharField(max_length=100)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="anewjob/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')

class OneJob(BaseModel):
    subject = models.CharField(max_length=50)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="onejob/%Y/%m")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name