from rest_framework import serializers
from shop.models import Shop
from common.api.serializers import SubCategorySerializer
from common.models import get_absolute_text

class ShopSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True,read_only=True,)
    pdf_url = serializers.SerializerMethodField('get_pdf_url')
    cover_url = serializers.SerializerMethodField('get_cover_url')
    description = serializers.SerializerMethodField('get_absolute_description')

    class Meta:
        model = Shop
        fields = ['title','cover_url','description','pdf_url','price','subcategories',]

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        pdf_url = obj.pdf_file.url
        return request.build_absolute_uri(pdf_url)

    def get_cover_url(self, obj):
        request = self.context.get('request')
        cover_url = obj.cover_img.url
        return request.build_absolute_uri(cover_url)

    # get_absolute_description
    def get_absolute_description(self, model):
        text = get_absolute_text(model.description)
        return text