from django.db import models
import uuid

# TODO make all contacts into mobile numbers or emails?


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    group_relation = models.ForeignKey('self', on_delete=models.CASCADE) # if groups want to belong together TODO make better abstraction
    contact = models.CharField(max_length=128)
    num_kids = models.IntegerField(default=0)
    num_adults = models.IntegerField(default=0)
    name = models.CharField(max_length=1024)
    wish_city = models.CharField(max_length=1024)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Accomodation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    rooms = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=1)
    bath = models.IntegerField(default=1)
    max_kids = models.IntegerField(default=0)
    max_adults = models.IntegerField(default=0)

    class Meta:
        ordering = ['rooms']

    def __str__(self):
        return f'{self.rooms}:{self.kitchen}:{self.bath} {self.max_adults}:{self.max_kids}'


class Driver(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=1024)
    contact = models.CharField(max_length=128)
    car = models.CharField(max_length=128)
    seats = models.IntegerField(default=1)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Notifier(models.Model):
    name = models.CharField(max_length=1024)
    contact = models.CharField(max_length=128)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# class Person(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     name = models.CharField(max_length=1024, nullable=True)
#     first_name = models.CharField(max_length=1024, nullable=True)
#     gender = models.CharField(
#         max_length=1,
#         choices=[
#             ('m', 'male'),
#             ('f', 'female'),
#             ('u', 'unknown'),
#         ],
#         default='u',
#     )
#     adult = models.BooleanField(
#         default=True
#     )
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
