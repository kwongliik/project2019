from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal
from django.contrib.auth.models import User


class Pembekal(models.Model):
    pembekal = models.CharField(max_length=30, unique=True)
    alamat = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)

    def __str__(self):
        return self.pembekal


class Stok(models.Model):
    stok = models.CharField(max_length=30)
    pembekal = models.ForeignKey(Pembekal, on_delete=models.CASCADE, related_name='stoks')

    def __str__(self):
        return self.stok

class Inventori(models.Model):
    inventori = models.CharField(max_length=50)
    stok = models.ForeignKey(Stok, on_delete=models.CASCADE, related_name='inventoris')
    harga = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01')),MaxValueValidator(Decimal('100.00'))])
    kuantiti = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventoris')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.inventori