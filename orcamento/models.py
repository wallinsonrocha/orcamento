from django.db import models
# Create your models here.


class Servico(models.Model):
    name = models.CharField(max_length=65)
    value = models.FloatField()
    total_value = models.FloatField()

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=65)
    value = models.FloatField()
    quantity = models.IntegerField()
    total_value = models.FloatField()

    def __str__(self):
        return self.name


class Orcamento(models.Model):
    name = models.CharField(max_length=65)
    client = models.CharField(max_length=65)
    description = models.CharField(max_length=125)
    servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name="orcamento_sv"
    )
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name="orcamento_mt"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

    # Falta continuar a partir do admin