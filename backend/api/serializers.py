from users.models import User, Freelancer, Recruiter
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = '__all__'

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'