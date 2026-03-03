from django.db import models


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('picked', 'Picked Up'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)

    pickup_address = models.TextField()
    delivery_address = models.TextField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    rider = models.ForeignKey(
        'Rider',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
    def save(self, *args, **kwargs):
        if self.rider and self.status == 'pending':
            self.status = 'assigned'
        super().save(*args, **kwargs)

class Rider(models.Model):

    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('busy', 'Busy'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='offline'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
