from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Library(models.Model):
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Userbook(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_id = models.ForeignKey(Library, on_delete=models.CASCADE)
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
    book_id = models.ManyToManyField(Book, on_delete=models.CASCADE)


class Group_study(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user_id = models.ManyToManyField(User, on_delete=models.CASCADE)
    library_id = models.ManyToManyField(Library, on_delete=models.CASCADE)


class Group_study_session(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    group_study_id = models.ForeignKey(Group_study, on_delete=models.CASCADE)
class Book(models.Model):
    author = models.ManyToManyField(Author)
    editors = models.ManyToManyField(User, through='editor')
    collections = models.ManyToManyField(User, through='collection')
    genre = models.ManyToManyField(Genre, through='genre')
    image = models.ImageField(upload_to='images/')

class Genre(models.Model):
    book_id = models.ManyToManyField(Book, on_delete=models.CASCADE)

class Author(models.Model):
    book_id = models.ManyToManyField(Book, on_delete=models.CASCADE)
