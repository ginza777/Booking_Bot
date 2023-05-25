from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django.utils.translation import gettext_lazy as _
from apps.common.models import Country, Region
from core.settings.base import LANGUAGES


def get_language_button():
    buttons = []
    for language in LANGUAGES:
        buttons.append([InlineKeyboardButton(str(_(language[1])), callback_data=language[0])])

    return InlineKeyboardMarkup(buttons)


def get_position_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("Exibitor")), callback_data='exibitor'),
            InlineKeyboardButton(str(_("Visitor")), callback_data='visitor'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def get_country_button():
    countries = Country.objects.all()
    buttons = []
    res = []
    for country in countries:
        res.append(InlineKeyboardButton(str(_(country.name)), callback_data=country.id))
        if len(res) == 2:
            buttons.append(res)
            res = []
    if len(res) >= 1:
        buttons.append(res)
    return InlineKeyboardMarkup(buttons)


def invite_to_channel_link():
    buttons = [
        [
            InlineKeyboardButton(str(_("Invite")), url='https://t.me/uicgroup'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)


# visitor

def get_region_button(country_id: int):
    regions = Region.objects.filter(country_id=country_id)
    buttons = []
    res = []
    for region in regions:
        res.append(InlineKeyboardButton(str(_(region.name)), callback_data=region.id))
        if len(res) == 2:
            buttons.append(res)
            res = []
    if len(res) >= 1:
        buttons.append(res)

    return InlineKeyboardMarkup(buttons)


def get_personality_type_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("Legal")), callback_data='Legal'),
            InlineKeyboardButton(str(_("Physical")), callback_data='Physical'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)
