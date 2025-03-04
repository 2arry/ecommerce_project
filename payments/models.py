from django.db import models

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment {self.payment_id} for Order {self.order.order_id}'
