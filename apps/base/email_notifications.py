from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader
import threading

# Envío de emails
def sendEmail(email, subject, template, data):
    current_template = loader.get_template(template)
    content = current_template.render(data)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_FROM,
        to=[email],
        cc=[]
    )

    message.attach_alternative(content, 'text/html')
    message.send()

# Envío de Notificaciones (Envia Emails en Segundo Plano)
def sendNotification(email, subject, template, data):
    thread = threading.Thread(target=sendEmail, args=(email, subject, template, data,))
    thread.start()