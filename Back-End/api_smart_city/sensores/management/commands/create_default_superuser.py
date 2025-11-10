from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self,*args,**options):
        username = "kauan"
        password = "12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username,email="",password=password)
            self.stdout.write(self.style.SUCCESS("Usuário 'kauan' criado! Sua senha atual é 12345"))
        else:
            self.stdout.write("Usuário já existe")