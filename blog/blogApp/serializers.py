from rest_framework import serializers
from blogApp.models import Category, Blog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Blog
        fields = '__all__'