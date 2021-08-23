from celery import task
from django.core.email import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order: {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfully placed an order.' \
    mail_sent = send_mail(subject, message, 'admin@config.com', [order.email])
    return mail_sent

