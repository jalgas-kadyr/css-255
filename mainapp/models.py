from django.db import models


class Object(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    describe = models.CharField(max_length=500)
    price = models.IntegerField()
    type = models.CharField(max_length=20)
    picture = models.CharField(max_length=10)


class Food(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)
    describe = models.CharField(max_length=500)
    price = models.IntegerField()
    type = models.CharField(max_length=20)
    picture = models.CharField(max_length=10)

    def __init__(self, code, name, describe, price, type):
        self.code = code
        self.name = name
        self.describe = describe
        self.price = price
        self.type = type

    def __str__(self):
        return self.name


