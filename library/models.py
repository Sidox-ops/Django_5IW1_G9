from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    # users = models.ManyToManyField(User,through='Userbook')
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Users = models.ManyToManyField(User)
    Books = models.ManyToManyField(Book)

class Userbook(models.Model):
    status = models.CharField(max_length=100)
    dateStart = models.DateTimeField(auto_now_add=True)
    dateEnd = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class Editor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return u'%s' % self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return u'%s' % self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return u'%s' % self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    def __str__(self):
        return u'%s' % self.name

