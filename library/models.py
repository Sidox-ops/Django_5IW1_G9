from django.db import models


class User(models.Model):
    surname = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Library(models.Model):
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Userbook(models.Model):
    status = models.CharField(max_length=100)
    dateStart = models.DateTimeField(auto_now_add=True)
    dateEnd = models.DateTimeField(auto_now_add=True)


class Editor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)




class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Group_study(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Group_study_session(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


