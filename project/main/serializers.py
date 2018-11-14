from django.contrib.auth.models import User, Group
from main.models import Advert
from rest_framework import serializers

app_name = 'main'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )

class AdvertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ('id', 'title', 'address', 'description', 'price', 'number_of_views', 'owner')
        owner = UserSerializer(read_only=True)


