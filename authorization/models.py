from django.db import models

# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     birthdate = models.DateField()

# class Book(models.Model):
#     title = models.CharField(max_length=30)
#     publication_date = models.DateField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#many to many relationship

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     courses = models.ManyToManyField('Course')

# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()

#one to one relationship

# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)

# class Profile(models.Model):
#     bio = models.TextField()
#     person = models.OneToOneField(Person, on_delete=models.CASCADE)