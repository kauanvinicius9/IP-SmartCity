import pandas as pd
from django.core.management.base import BaseCommand
from sensores.models import Local

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument("arquivo",type=str)

    def handle(self,*args,**options):
        path = options["arquivo"]
        
        try:
            df = pd.read_csv(path, encoding="utf-8-sig")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao ler CSV {e}"))
            
        if "local" not in df.columns and "Local" not in df.columns:
             self.stderr.write(self.style.ERROR("Seu arquivo precisa ter uma coluna chamada 'local' ou 'Local'"))
             return
         
        counter = 0
        for _, row in df.iterrows():
            local = str(row.get("local") or row.get("Local") or "").strip()
            if local:
                Local.objects.get_or_create(nome=local)
                counter += 1
            
        self.stdout.write(self.style.SUCCESS(f"{counter} Locais importados com sucesso!"))