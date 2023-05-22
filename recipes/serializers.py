from rest_framework import serializers

from .models import Dish


class DishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Dish
        fields = "__all__"
