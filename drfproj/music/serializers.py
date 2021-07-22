# SerializerMethodField:
# This is a read-only field. It gets its value by
# calling a method on the serializer class it is attached to. It can be used to add any sort of data to the serialized representation of your object.


# We can add or edit attributes of a model, we can use SerializerMethodField

from django.utils.timezone import now
from rest_framework import serializers
# from rest_framework import serializers
from music.models import Music, Student


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()


class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField('custom_method')    #new field
    singer = ToUpperCaseCharField() #edit attribute

    def custom_method(self, obj):   #obj-object to be serialized
        return (now() - obj.created).days

    class Meta:
        model = Music
        fields = ('id', 'song','place',  'singer', 'last_modify_date', 'genre',  'created', 'days_since_created')
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')

    


class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = ['id', 'name', 'email'] 