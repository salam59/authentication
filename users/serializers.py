from users.models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) # accesses the current model CustomUser
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class MyObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls,user):
        token = super(MyObtainTokenSerializer,cls).get_token(user)

        #custom claims

        token['user_type'] = user.user_type
        token['user_name'] = user.username
        return token