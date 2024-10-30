from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(required=False)
    status_display = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'user', 'nome', 'descricao', 'status', 'status_display', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def get_status_display(self, obj):  
        return "concluída" if obj.status else "pendente"
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    




