from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


    def mark_as_concluida(self):
        self.status = True
        self.save()

    def mark_as_pendente(self):
        self.status = False
        self.save()






