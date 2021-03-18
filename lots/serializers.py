from django.contrib.auth.models import User, Group
from rest_framework import serializers

from lots.models import Lots, Category, Pages, CategoryFilter

class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class LotDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.ChoiceField(choices=Lots.STATUS_OF_LOT)
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Lots
        fields = '__all__'


class PagesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = '__all__'


class PagesSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pages
        fields = '__all__'


class LotsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lots
        fields = ('id', 'name', 'category', 'user')


class CategoryFilterSerializer(serializers.ModelSerializer):
    field1 = serializers.ChoiceField(
            choices=['red', 'green', 'blue'], )
    field2 = serializers.ChoiceField(
            choices=['red', 'green', 'blue'], )

    class Meta:
        model = CategoryFilter
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

    # def get_count(self, obj):
    #     return obj.cat.all().count()

    # def get_filter(self, obj):
    #     return obj.categoryfilter_set.all()


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']