# coding=utf-8
# register
import os
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.template import Context


EMAIL_TEMPLATE = '/template/email/'


# TODO 在settings下面配置邮件相关参数
# 单发 群发
def send_mail(to_email, type='register'):
    """
    :param to_email:
    :param type: 邮件类型
    :return:
    """
    subject = ""
    to = [to_email]
    from_email = settings.DEFAULT_FROM_EMAIL

    ctx = {
        'user': 'buddy',
        'link': ''
    }

    templat_path = os.path.join(EMAIL_TEMPLATE, type + '.html')
    body = get_template(templat_path).render(Context(ctx))
    msg = EmailMessage(subject, body, from_email=from_email, to=to)
    msg.content_subtype = 'html'
    try:
        msg.send()
    except Exception:
        # TODO 打印日志



        return False
    return True



# forget_pwd


