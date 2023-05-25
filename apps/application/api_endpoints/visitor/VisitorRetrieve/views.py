import mimetypes

from django.http import FileResponse
from rest_framework.generics import RetrieveAPIView

from apps.application.api_endpoints.visitor.VisitorRetrieve.serializers import \
    VisitorDetailSerializer
from apps.application.models import Visitor


class RetrieveVisitorTicketAPIView(RetrieveAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_field = instance.visitor_ticket.pdf

        response = FileResponse(file_field.open(), as_attachment=True)

        content_type, _ = mimetypes.guess_type(file_field.name)
        response["Content-Type"] = content_type

        response["Content-Disposition"] = 'attachment; filename="{}"'.format(file_field.name)

        return response
