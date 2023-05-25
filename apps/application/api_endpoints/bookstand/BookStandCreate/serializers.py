from rest_framework import serializers

from apps.application.models import BookStand, HearingUs


class BookStandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStand
        fields = ("id", "name", "company_name", "country", "phone", "email", "hear_us")


class HearingUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HearingUs
        fields = ("id", "title")