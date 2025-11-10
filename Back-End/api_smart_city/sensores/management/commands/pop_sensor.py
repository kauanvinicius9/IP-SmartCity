import pandas as pd
from django.core.management.base import BaseCommand
from sensores.models import Sensor

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
        
        if "sensor" not in df.columns and "Sensor" not in df.columns:
             self.stderr.write(self.style.ERROR(f"Seu arquivo precisa ter uma coluna chamada 'sensor' ou ' Sensor'"))
             return
         
        counter = 0
        for _, row in df.iterrows():
            sensor = str(row.get("sensor") or row.get("Sensor") or "").strip()
            if sensor :
               Sensor.objects.get_or_create(
                   tipoSensor=sensor,
                   identifSensor=f"{sensor.lower()}_{counter}",
                )
               
               counter += 1
        
        self.stdout.write(self.style.SUCCESS(f"{counter} sensores importados com sucesso!"))