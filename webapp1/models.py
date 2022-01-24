from django.db import models
import pyqrcode
import png
from pyqrcode import QRCode
# Create your models here.
from django.utils.html import mark_safe
from datetime import datetime
from PIL import Image
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.core.files.base import ContentFile
import io
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.sites.shortcuts import get_current_site


class Verifica_Risultati_Candidato(models.Model):
    class Meta:
        verbose_name_plural = 'Verifica Risultati Candidato'

    MATRICOLA = models.IntegerField()
    COGNOME = models.CharField(max_length=255, blank=True, null=True)
    NOME = models.CharField(max_length=255, blank=True, null=True)
    DATA_DI_NASCITA = models.DateField(default=datetime.now(), blank=True)
    NAZIONALITA = models.CharField(max_length=255, blank=True, null=True)
    show_MATRICOLA = models.BooleanField(default=True)
    Auto_QR_Code = models.ImageField(blank=True, null=True, help_text='Auto Generate QR Code')

    @property
    def thumbnail_preview(self):
        if self.Auto_QR_Code:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.Auto_QR_Code.url))
        return ""

    def __str__(self):
        return str(self.MATRICOLA)


    def save(self, *args, **kwargs):
        print('when save')
        print(self.MATRICOLA)
        site = get_current_site(self.request)
        domain_name=site.domain
        print(domain_name)
        s = f"http://www.localhost:8000/student_page/{self.MATRICOLA}"
        url = pyqrcode.create(s)
        url.png(f'qrcodes/{self.MATRICOLA}.png', scale=6)
        try:
            path = f"{BASE_DIR}\qrcodes\{self.MATRICOLA}.png"
            image = Image.open(path)
            image = image.convert('RGB')
            image = image.resize((800, 800), Image.ANTIALIAS)
            output = io.BytesIO()
            image.save(output, format='JPEG', quality=85)
            output.seek(0)

            main_img = InMemoryUploadedFile(output, 'ImageField', f"{BASE_DIR}\qrcodes_new\{self.MATRICOLA}.jpg", 'image/jpeg', sys.getsizeof(output), None)
            print(main_img)
            self.Auto_QR_Code = main_img
        except IOError:
            pass
        super(Verifica_Risultati_Candidato, self).save(*args, **kwargs)


class Esami_sostenuti_e_relativi_esiti(models.Model):
    class Meta:
        verbose_name_plural = 'Esami sostenuti e relativi esiti'
    Student = models.ForeignKey(Verifica_Risultati_Candidato, on_delete=models.CASCADE, default=None)
    Sessione = models.CharField(max_length=255, blank=True, null=True)
    Data = models.DateField(default=datetime.now(), blank=True)
    Esame = models.CharField(max_length=255, blank=True, null=True)
    Centro = models.CharField(max_length=255, blank=True, null=True)
    Parte = models.CharField(max_length=255, blank=True, null=True)
    Esito = models.CharField(max_length=255, blank=True, null=True)
    Note_appello = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Sessione