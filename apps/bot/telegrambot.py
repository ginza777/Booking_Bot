import logging
from telegram import Update
from telegram.ext import CallbackContext
from django.utils.translation import gettext_lazy as _, activate
from apps.bot import models
from utils.decarators import get_member
from .buttons.inline import get_language_button, get_position_button, get_country_button, invite_to_channel_link, \
    get_region_button, get_personality_type_button
from .buttons.keyboard import get_phone_number_button
from .state import state
from telegram import ReplyKeyboardRemove

logger = logging.getLogger(__name__)
from apps.application.models import Visitor, BookStand, Ticket



@get_member
def start(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    """Send a message when the command /start is issued."""
    update.message.reply_text(str(_("Assalomu alaykum Automative botimizga xush kelibsiz")),
                              reply_markup=get_language_button())

    return state.GET_LANGUAGE


@get_member
def get_language(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    tg_user.language = query.data
    context.user_data['language'] = query.data
    tg_user.save()
    activate(tg_user.language)
    query.edit_message_text(str(_("Quyidagi tanlovlardan birini tanalang (exhibitor/visitor)")),
                            reply_markup=get_position_button())

    return state.GET_USER_TYPE


@get_member
def get_user_type_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['user_type'] = query.data
    query.edit_message_text(str(_("F.I.Sh ni kiriting:")))
    return state.GET_FULL_NAME_EXIBITOR


@get_member
def get_full_name_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['full_name'] = update.message.text
    message = update.message.reply_text(text=str(_("Kompaniyanigizni nomini kiriting:")))
    return state.GET_COMPANY_NAME_EXIBITOR


@get_member
def get_company_name(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['company_name'] = update.message.text
    update.message.reply_text(text=str(_("Quyidagi davlatlardan birini tanlang ")), reply_markup=get_country_button())
    return state.GET_COUNTRY_NAME_EXIBITOR


@get_member
def get_country_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['country_id'] = query.data
    query.delete_message()
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(_("Telefon raqamingizni yuboring:")),
                             reply_markup=get_phone_number_button())
    return state.GET_PHONE_NUMBER_NAME_EXIBITOR


@get_member
def get_phone_number_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['phone_number'] = update.message.contact.phone_number
    update.message.reply_text(text=str(_("Emailingizni yuboring: ")), reply_markup=ReplyKeyboardRemove())
    return state.GET_EMAIL_EXIBITOR


@get_member
def get_email_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['email'] = update.message.text
    exibitor = BookStand.objects.create(
        name=context.user_data['full_name'],
        company_name=context.user_data['company_name'],
        country_id=context.user_data['country_id'],
        phone=context.user_data['phone_number'],
        email=context.user_data['email'],
    )
    exibitor.save()
    update.message.reply_text(str(_("Rahmat siz muaffaqiyatli ro'yxatdan o'tdingiz siz bilan bog'lanamiz")),
                              reply_markup=invite_to_channel_link())
    update.message.reply_text(str(_("Quyidagilardan birini tanlang:")), reply_markup=get_position_button())
    return state.GET_USER_TYPE


# ________________________________ visitor registration___________________________________________________________________________________________________________________________


@get_member
def get_user_type_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['user_type'] = query.data
    query.edit_message_text(str(_("Ismingizni kiriting:")))
    return state.GET_NAME_VISITOR


@get_member
def get_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['name'] = update.message.text
    update.message.reply_text(str(_("Familyangizni kiriting:")))
    return state.GET_SURNAME_VISITOR


@get_member
def get_surname_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['surname'] = update.message.text
    update.message.reply_text(str(_("Davlatingizni tanlang ")), reply_markup=get_country_button())
    return state.GET_COUNTRY_VISITOR


@get_member
def get_country_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['country_id'] = query.data
    query.edit_message_text(str(_("Viloyatni tanlang")),
                            reply_markup=get_region_button(context.user_data['country_id']))
    return state.GET_REGION_VISITOR


@get_member
def get_region_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['region_id'] = query.data
    query.edit_message_text(str(_("Personality type:")), reply_markup=get_personality_type_button())
    return state.PERSONALITY_TYPE_VISITOR


@get_member
def personality_type_visitors(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    context.user_data['personality_type'] = query.data
    query.delete_message()
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(_("Telefon raqamingizni yuboring:")),
                             reply_markup=get_phone_number_button())
    return state.GET_PHONE_NUMBER_VISITOR


@get_member
def get_phone_number_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['phone_number'] = update.message.contact.phone_number
    update.message.reply_text(text=str(_("Emailingizni yuboring:")), reply_markup=ReplyKeyboardRemove())
    return state.GET_EMAIL_VISITOR


@get_member
def get_email_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    context.user_data['email'] = update.message.text

    visitor = Visitor.objects.create(
        first_name=context.user_data['name'],
        last_name=context.user_data['surname'],
        country_id=context.user_data['country_id'],
        region_id=context.user_data['region_id'],
        phone=context.user_data['phone_number'],
        email=context.user_data['email'],
        personality=context.user_data['personality_type'],
    )

    visitor.save()
    file = Ticket.objects.get(visitor=visitor).pdf.path
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(f"{file}", 'rb'),
                              caption=str(_("Your ticket")))
    update.message.reply_text(str(_("thanks for registration")), reply_markup=invite_to_channel_link())
    update.message.reply_text(str(_("Quyidagilardan birini tanlang:")), reply_markup=get_position_button())

    return state.GET_USER_TYPE
