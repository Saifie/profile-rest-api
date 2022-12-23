from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serial for field na,e hellow apis"""
    name = serializers.CharField(max_length=10)
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile"""
    class Meta:
        model=models.UserProfile
        fields=('id', 'name', 'email', 'password')
        
        extra_kargs = {
            'password': {
                'write_only': True,
                'style':{
                'input_type': 'password',
                }
            
            }
        
        }
    def create(self, validated_data):
        """Create user profile"""
        user= models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )
        return user
class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializer for feeds"""
    class Meta:
        model=models.ProfileFeedModel
        fields=('id','user_profile','status_text')
        extra_kargs = {
            'user_profile': {
                'read_only': True,
            }
        
        }