from rest_framework import serializers

from apps.application.models import Visitor


class VisitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = (
            "id",
            "first_name",
            "last_name",
            "country",
            "region",
            "personality",
            "company_name",
            "job_title",
            "website",
            "phone",
            "email",
            "service",
            "activity",
            "feedback",
        )
