from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

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

    def __str__(self):
        return self.name



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
        return self.board.name+" "+str(self.year)

"""Question Type"""
class QuestionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""Question"""
options = [
    (1,1), (2,2), (3,3),(4,4),
]
class Question(models.Model):
    published = models.BooleanField(default=False)
    question_body = RichTextUploadingField()
    option1 = RichTextUploadingField()
    option2 = RichTextUploadingField()
    option3 = RichTextUploadingField()
    option4 = RichTextUploadingField()
    answer_number = models.PositiveIntegerField(choices=options,validators=[MinValueValidator(1), MaxValueValidator(4)])
    solution = RichTextUploadingField()
    subcategories = models.ManyToManyField(SubCategory)
    chapters = models.ManyToManyField(Chapter)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    histories = models.ManyToManyField(QuestionHistory,blank=True)
    types = models.ManyToManyField(QuestionType)


    def __str__(self):
        return mark_safe(self.question_body)

    def question_body_field(self):
            return mark_safe(self.question_body)

    question_body_field.short_description = 'Question Body'
