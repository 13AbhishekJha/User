from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'company_name', 'age', 'city', 'state', 'zip', 'email', 'web']

    def validate(self, data):
        email = data.get('email')
        if email:
            existing_users = User.objects.filter(email=email)
            if self.instance:  # If updating an existing instance
                existing_users = existing_users.exclude(pk=self.instance.pk)
            if existing_users.exists():
                raise serializers.ValidationError("Another user with this email already exists.")
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.email = validated_data.get('email', instance.email)
        instance.web = validated_data.get('web', instance.web)
        instance.save()
        return instance