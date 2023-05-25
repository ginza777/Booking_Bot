import os

import qrcode
from django.shortcuts import render
from django.template import loader

from apps.application.models import Visitor
from core.settings.base import BASE_DIR, SITE_DOMAIN


def ticket(request):
    obj = Visitor.objects.first()
    site_url = f"{SITE_DOMAIN}/api/v1/application/VisitorDetail/{obj.id}/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2,
    )
    qr.add_data(site_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    file = os.path.join(BASE_DIR, "media", "qr_code", f"qrcode_{obj.id}.png")
    img.save(file)
    template = loader.get_template("index.html")
    image_url = f"{SITE_DOMAIN}/media/qr_code/{f'qrcode_{obj.id}.png'}"
    context = {
        "id": obj.id,
        "first_name": obj.first_name,
        "last_name": obj.last_name,
        "company_name": obj.company_name,
        "job_title": obj.job_title,
        "personality": obj.personality,
        "qr_code": image_url,
    }

    return render(request, "index.html", context)
