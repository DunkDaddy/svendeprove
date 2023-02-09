from rest_framework import serializers
from .models import *


class PostNummerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostNummer
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class HandlingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handlinger
        fields = '__all__'


class HandlingJunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handling_Junctions
        fields = '__all__'


class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'


class RapporjunctionstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport_junctions
        fields = '__all__'


class PointGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointGrade
        fields = '__all__'


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'


class Uddel_PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uddel_Permissions
        fields = '__all__'


class BPID(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['brugernavn', 'password']

