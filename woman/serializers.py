from rest_framework import serializers
from .models import Woman
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
# class WomanSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Woman
#         fields = ('id', 'title', 'content', 'created', 'updated', 'published', 'category')
#         # fields = ('title', 'category')

# class WomanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomanSerializers(serializers.Serializer):
    id = serializers.CharField(read_only = True)
    title = serializers.CharField(max_length = 100)
    content = serializers.CharField()
    created = serializers.TimeField(read_only = True)
    updated = serializers.TimeField(read_only = True)
    published = serializers.BooleanField(default=True)
    category_id = serializers.CharField()

    def create(self, validated_date):
        return Woman.objects.create(**validated_date)

# def encode():
#     model = WomanModel('Title', 'Content: content')
#     model_sr = WomanSerializers(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Title","content":"Content: content"}')
#     data = JSONParser().parse(stream)
#     serializer = WomanSerializers(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)