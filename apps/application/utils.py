import os
import tempfile

import qrcode
import weasyprint
from django.core.files.base import ContentFile
from django.template import loader

from apps.application.models import Ticket, TicketInfo
from core.settings.base import MEDIA_ROOT, SITE_DOMAIN


def generate_ticket(obj):
    info = TicketInfo.objects.first()
    site_url = f"{SITE_DOMAIN}/api/v1/application/VisitorDetail/{obj.id}"

    qr = qrcode.make(site_url)

    qr_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    qr.save(qr_file.name)

    template = loader.get_template("index.html")
    context = {
        "id": obj.id,
        "first_name": obj.first_name,
        "last_name": obj.last_name,
        "company_name": obj.company_name,
        "job_title": obj.job_title,
        "personality": obj.personality,
        "qr_code": qr_file.name,
        "info": info,
    }
    html = template.render(context)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        tmp_file.write(html.encode("utf-8"))
        tmp_file.flush()

        pdf_file = weasyprint.HTML(filename=tmp_file.name).write_pdf()

        file_name = f"qr_code_{obj.id}.pdf"
        file_path = os.path.join(MEDIA_ROOT, "ticket", file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(pdf_file)

        ticket = Ticket.objects.create(visitor=obj)
        ticket.pdf.save(file_name, ContentFile(pdf_file), save=True)

    os.unlink(qr_file.name)
