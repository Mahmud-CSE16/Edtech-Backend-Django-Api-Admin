from rest_framework import serializers
from goniter_itihash.models import GoniterItihash
from common.models import get_absolute_text

class GoniterItihashSerializer(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField('get_cover_url')
    description = serializers.SerializerMethodField('get_absolute_description')

    class Meta:
        model = GoniterItihash
        fields = ['title','cover_url','description',]

    def get_cover_url(self, obj):
        request = self.context.get('request')
        cover_url = obj.cover_img.url
        return request.build_absolute_uri(cover_url)

     # get_absolute_description
    def get_absolute_description(self, model):
        text = get_absolute_text(model.description)
        return text