from rest_framework import serializers
from bigoto_bochor.models import BigotoBochor
from common.api.serializers import SubCategorySerializer, QuestionHistorySerializer

class BigotoBochorSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True,)
    question_history = QuestionHistorySerializer(read_only=True)
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = BigotoBochor
        fields = ['id','subcategory','question_history','pdf_url',]

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        pdf_url = obj.pdf_file.url
        return request.build_absolute_uri(pdf_url)

    