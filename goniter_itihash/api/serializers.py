from rest_framework import serializers
from goniter_itihash.models import GoniterItihash

class GoniterItihashSerializer(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField('get_cover_url')

    class Meta:
        model = GoniterItihash
        fields = ['title','cover_url','description',]

    def get_cover_url(self, obj):
        request = self.context.get('request')
        cover_url = obj.cover_img.url
        return request.build_absolute_uri(cover_url)