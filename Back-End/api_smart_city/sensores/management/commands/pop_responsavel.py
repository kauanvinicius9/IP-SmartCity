import pandas as pd
from django.core.management.base import BaseCommand
from sensores.models import Responsavel

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument("arquivo",type=str)

    def handle(self,*args,**options):
        path = options["arquivo"]
        
        try:
            df = pd.read_csv(path, encoding="utf-8-sig")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao ler CSV {e}"))
            return
        
        if "nome" not in df.columns and "Nome" not in df.columns:
             self.stderr.write(self.style.ERROR(f"Seu arquivo precisa ter uma coluna chamada 'nome' ou ' Nome'"))
             return
         
        counter = 0
        for _, row in df.iterrows():
            nome = str(row.get("nome") or row.get("Nome") or "").strip()
            if nome :
                Responsavel.objects.get_or_create(nome=nome)
                counter += 1
        
        self.stdout.write(self.style.SUCCESS(f"{counter} responsáveis importados com sucesso!"))