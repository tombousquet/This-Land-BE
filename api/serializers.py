from rest_framework import serializers
from core.models import PointOfInterest, TellYourStory

class TYSSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = TellYourStory
        fields = [
            'user',
            'id',
            'text',
            'images',
            'date_created',
            'poi',
        ]

class POISerializer(serializers.ModelSerializer):
    TellYourStories = TYSSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = PointOfInterest
        fields = [
            'user',
            'id',
            'location_name',
            'notes',
            'street_address',
            'city',
            'state',
            'zip_code',
            'images',
            'category',
            'date_created',
            'TellYourStories',
        ]