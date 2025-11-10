import pandas as pd
from django.core.management.base import BaseCommand
from sensores.models import Historico, Sensor, Ambiente

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument("arquivo",type=str)

    def handle(self,*args,**options):
        path = options["arquivo"]
        
        try:
            df = pd.read_csv(path, encoding="utf-8-sig")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao ler CSV {e}"))
            
        required = ["sensor", "valor", "ambiente"]
        for column in required:
            if column not in df.columns:
                self.stderr.write(self.style.ERROR(f"O arquivo precisa da coluna {column}"))
                return
                
        counter = 0
            
        for _, row in df.iterrows():
            try:
                sensor_id = int(row["sensor"])
                valor = str(row["valor"]).strip()
                ambiente_id = int(row["ambiente"])
                
                sensor = Sensor.objects.filter(idSensor=sensor_id).first()
                ambiente = Ambiente.objects.filter(id=ambiente_id).first()
                
                if not sensor:
                    self.stderr.write(self.style.WARNING(f"Sensor ID {sensor_id} não identificado"))
                    continue
                
                if not ambiente:
                    self.stderr.write(self.style.WARNING(f"Ambiente ID {ambiente_id} não identificado"))
                    continue
                
                Historico.objects.get_or_create(
                    sensor=sensor,
                    valor=valor,
                    ambiente=ambiente
                )
                
                counter += 1
                
            except Exception as e:
                  self.stderr.write(self.style.ERROR(f"Erro ao exibir a linha {e}"))
                  
        self.stdout.write(self.style.SUCCESS(f"{counter} históricos importados com sucesso!"))