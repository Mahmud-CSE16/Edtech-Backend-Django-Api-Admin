from rest_framework import serializers


from question.models import McqQuestion
from topic_vittic_porashona.models import TopicVitticPorashona
from common.models import get_absolute_text
from question.api.serializers import McqQuestionSerializer


class TopicVitticPorashonaSerializer(serializers.ModelSerializer):

    
    description = serializers.SerializerMethodField('get_absolute_description')
    cover_url = serializers.SerializerMethodField('get_cover_url')
    questions = McqQuestionSerializer(many=True)
    

    class Meta:
        model = TopicVitticPorashona
        fields = ['title','cover_url','description','questions',]

    
   
    # get_absolute_body
    def get_absolute_description(self, obj):
        text = get_absolute_text(obj.description)
        return text

    def get_cover_url(self, obj):
        request = self.context.get('request')
        cover_url = obj.cover_img.url
        return request.build_absolute_uri(cover_url)






