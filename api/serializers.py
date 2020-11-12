from rest_framework import serializers
from .models import User,Group

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields ='__all__'

	def create(self, validated_data):
		return User.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields ='__all__'

	def create(self, validated_data):
		return Group.objects.create(**validated_data)
