from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='https://via.placeholder.com/150')
class Library(models.Model):
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Users = models.ManyToManyField(User)
    Books = models.ManyToManyField(Book)

class Userbook(models.Model):
    status = models.CharField(max_length=100)
    dateStart = models.DateTimeField(auto_now_add=True)
    dateEnd = models.DateTimeField(auto_now_add=True)
    user = models.OneToManyField(User)
    book = models.ManyToManyField(Book)


class Editor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)


class Group_study(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    library = models.ManyToManyField(Library)

class Group_study_session(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    group_study = models.ManyToManyField(Group_study)



