from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Location(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    is_depot = models.BooleanField(default=False, help_text="Define se o local é um ponto de origem/retorno (Sede, Silo, etc).")

    class Meta:
        verbose_name = "Location"
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name} ({'Depot' if self.is_depot else 'Point'})"
    
class Machine(models.Model):

    class OperationType(models.TextChoices):
        HARVEST = 'harvest', 'Colheita'
        TRANSPORT = 'transport', 'Transporte'
        SPRAYING = 'spraying', 'Pulverização'

    name = models.CharField(max_length=100)
    capacity_kg = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.1)]
    )
    speed_kmh = models.FloatField(
        validators=[MinValueValidator(0.1)],
        help_text="Velocidade média operacional para cálculo de tempo de rota."
    )   
    fuel_consumption_lh = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name="Consumo (L/h)"
    )
    operation_type = models.CharField(
        max_length=20,
        choices=OperationType.choices,
        default=OperationType.HARVEST
    )

    class Meta:
        verbose_name = "Machine"

    def __str__(self) -> str:
        return f"{self.name} [{self.get_operation_type_display()}]"