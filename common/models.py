from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

"""Category Class"""
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

"""SubCategory Class"""
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('category__name','name')

    def __str__(self):
        return self.name+"-->"+self.category.name


"""Chapter Class"""
class Chapter(models.Model):
    name= models.CharField(max_length=255)
    number = models.IntegerField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name +"-->"+self.subcategory.name

    class Meta:
        ordering = ('subcategory__name','number',)
        constraints = [
            models.UniqueConstraint(fields=['name', 'subcategory'], name='chapter constraint')
        ]


"""Language"""
class Language(models.Model):
    name = models.CharField(max_length=255, unique=True,)

    def __str__(self):
        return self.name



"""Board"""
class Board(models.Model):
    name = models.CharField(max_length=255, unique=True,)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    class Meta:
        ordering = ('subcategory__name','name',)
        constraints = [
            models.UniqueConstraint(fields=['name', 'subcategory'], name='board constraint')
        ]

    def __str__(self):
        return self.name+"-->"+self.subcategory.name



"""Question History"""
def current_year():
    return datetime.date.today().year+1


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def year_choices():
    list = [(r,r) for r in range(1995, datetime.date.today().year+1)]
    list.reverse()
    return list


class QuestionHistory(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=year_choices(),default=current_year(), validators=[MinValueValidator(1995), max_value_current_year])


    class Meta:
        ordering = ('-year','board__name',)


    def __str__(self):
        return self.board.name+" "+str(self.year)+"-->"+self.board.subcategory.name

"""Question Type"""
class QuestionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

