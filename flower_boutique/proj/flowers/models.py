from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return f'{self.name}'


class Flowers(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    EXPIRED = "expired"

    STATUS_LIST = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (EXPIRED, 'expired')
    ]

    COLOR_CHOICES = [
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('white', 'White'),
        ('mixed', 'Mixed'),
    ]


    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,
                                null=True)
    

    title = models.CharField(max_length=64)
    description = models.TextField()
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    quantity = models.PositiveIntegerField()
    raiting = models.DecimalField(max_digits=2, decimal_places=1)

    status = models.CharField(
        choices=STATUS_LIST,
        default=PENDING,
        max_length=16,
        null=True
    )

    image = models.ImageField(upload_to="uploads/flowers", null=True)

    price_before_discount = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        null=True)
    
    price_after_discount = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
    
    
    @property
    def raiting_stars(self):
        full_stars = int(self.raiting)
        half_stars = self.raiting - full_stars
        stars = '★' * full_stars
        if half_stars:
            stars += '☆'
        stars = stars.ljust(5, '☆')
        return stars
    
    def save(self, *args, **kwargs):
        if not self.expires_at:            
            self.expires_at = timezone.now() + timedelta(days=30)
        return super().save(*args, **kwargs)
    
    
    def generate_url(self, request):
        relative_url = reverse("flower_details", kwargs={"flower_id": self.pk})
        return request.build_absolute_uri(relative_url)
