from django.contrib.auth.models import User, Group
from main.models import Task_List
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

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List
        fields = ('id', 'task_list_name', 'created_by', 'created_at')
# class TaskListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     task_list_name = serializers.CharField(required=True, allow_blank=False, max_length=200)
#     created_by = UserSerializer(read_only=True)
#     created_at = serializers.DateTimeField('date published')
#
#     def create(self, validated_data):
#         return Task_List.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.task_list_name = validated_data.get('task_list_name', instance.task_list_name)
#         instance.created_by = validated_data.get('created_by', instance.created_by)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.save()
#         return instance