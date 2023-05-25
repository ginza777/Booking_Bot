from rest_framework import serializers

from apps.application.models import Visitor, ChoiceOfService, ActivityOfYourCompany


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ("id", "first_name", "last_name", "country", "region", "personality", "company_name", "job_title",
                  "website", "phone", "email", "service", "activity", "feedback")


class ChoiceOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOfService
        fields = ("id", "title")


class ActivityOfYourCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityOfYourCompany
        fields = ("id", "title")
