from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # fields = ('__all__')
    fields = (
      'id',
      'username',      
      'first_name',
      'middle_name',
      'last_name',
      'preferred_name',
      'is_superuser',
      'email',
      'dob',
      'photo'
    )


class CustomRegisterSerializer(RegisterSerializer):
  first_name = serializers.CharField(
    required=False,
    allow_blank=True)
  middle_name = serializers.CharField(
    required=False,
    allow_blank=True)
  last_name = serializers.CharField(
    required=False,
    allow_blank=True)
  preferred_name = serializers.CharField(
    required=False,
    allow_blank=True)
  dob = serializers.DateField(
    required=False)
  photo = serializers.URLField(
    required=False,
    allow_blank=True)

  class Meta:
    model = User
    fields = (
      'email',
      'username',
      'password',
      'first_name',
      'middle_name',
      'last_name',
      'preferred_name',
      'dob',
      'photo'
    )

  def get_cleaned_data(self):
    return {
      "email":          self.validated_data.get("email", ""),      
      "username":       self.validated_data.get("username", ""),
      "password1":      self.validated_data.get("password1", ""),
      "password2":      self.validated_data.get("password2", ""),
      "first_name":     self.validated_data.get("first_name", ""),
      "middle_name":    self.validated_data.get("middle_name", ""),
      "last_name":      self.validated_data.get("last_name", ""),
      "preferred_name": self.validated_data.get("preferred_name", ""),
      "dob":            self.validated_data.get("dob", ""),
      "photo":          self.validated_data.get("photo", ""),
    }      

  def save(self, request):
    adapter = get_adapter()
    user = adapter.new_user(request)
    self.cleaned_data = self.get_cleaned_data()

    user.first_name     = self.cleaned_data.get("first_name")
    user.middle_name    = self.cleaned_data.get("middle_name")
    user.last_name      = self.cleaned_data.get("last_name")
    user.preferred_name = self.cleaned_data.get("preferred_name")
    user.save()
    adapter.save_user(request, user, self)
    return user

class TokenSerializer(serializers.ModelSerializer):
  user_data = serializers.SerializerMethodField()

  class Meta:
    model=Token
    fields = ("key", "user", "user_data")

  def get_user_data(self, obj):
    serializer_data = UserSerializer(
      obj.user
    ).data
    email          = serializer_data.get("email")
    username       = serializer_data.get("username")
    first_name     = serializer_data.get("first_name")
    middle_name    = serializer_data.get("middle_name")
    last_name      = serializer_data.get("last_name")
    preferred_name = serializer_data.get("preferred_name")
    photo          = serializer_data.get("photo")
    dob            = serializer_data.get("dob")
    return {
      "email":email,
      "username":username,
      "first_name":first_name,
      "middle_name":middle_name,
      "last_name":last_name,
      "preferred_name":preferred_name,
      "photo": photo,
      "dob": dob
    }