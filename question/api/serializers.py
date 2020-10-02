from rest_framework import serializers
from question.models import McqQuestion
from common.api.serializers import ChapterSerializer
from common.models import get_absolute_text



""" # replace to image full path
SEARCH_PATTERN = '/media/uploads/'
REPLACE_WITH = '%s/media/uploads/' % settings.SITE_DOMAIN
# replace to image full path
def get_absolute_text(value):
    text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
    return text """

class McqQuestionSerializer(serializers.ModelSerializer):

    body = serializers.SerializerMethodField('get_absolute_body')
    option1 = serializers.SerializerMethodField('get_absolute_potion1')
    option2 = serializers.SerializerMethodField('get_absolute_potion2')
    option3 = serializers.SerializerMethodField('get_absolute_potion3')
    option4 = serializers.SerializerMethodField('get_absolute_potion4')
    solution = serializers.SerializerMethodField('get_absolute_solution')
    chapters = ChapterSerializer(many=True)
    

    class Meta:
        model = McqQuestion
        fields = ['body','option1','option2','option3','option4','solution','answer_number','chapters']

    
    # get_absolute_body
    def get_absolute_body(self, question):
        text = get_absolute_text(question.question_body)
        return text


    # get_absolute_body
    def get_absolute_potion1(self, question):
        text = get_absolute_text(question.option1)
        return text

    # get_absolute_body
    def get_absolute_potion2(self, question):
        text = get_absolute_text(question.option2)
        return text

    # get_absolute_body
    def get_absolute_potion3(self, question):
        text = get_absolute_text(question.option3)
        return text

    # get_absolute_body
    def get_absolute_potion4(self, question):
        text = get_absolute_text(question.option4)
        return text

    # get_absolute_body
    def get_absolute_solution(self, question):
        text = get_absolute_text(question.solution)
        return text





