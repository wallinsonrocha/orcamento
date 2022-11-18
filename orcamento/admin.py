from django.contrib import admin
from . import models


@admin.register(models.Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Servico)
class ServicoAdmin(admin.ModelAdmin):
    ...
