from rest_framework import serializers
from .models import Responsavel, Ambiente, Local, Historico, Sensor

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = "__all__"

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = "__all__"

class AmbienteSerializer(serializers.ModelSerializer):
    local = LocalSerializer(read_only=True)
    local_id = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all(), source="local", write_only="True")
    class Meta:
        model = Ambiente
        fields = ["id", "local", "local_id", "responsavel", "descricao"]

class SensoresSerializer(serializers.ModelSerializer):
    ambiente = AmbienteSerializer(read_only=True)
    ambiente_id = serializers.PrimaryKeyRelatedField(queryset=Ambiente.objects.all(), source="ambiente", write_only=True, allow_null=True, required=False)
    class Meta:
        model = Sensor
        fields = ["id_sensor", "tipo", "unidade_med", "identificacao", "latitude", "longitude", "status", "ambiente", "ambiente_id", "timestamp"]
        read_only_fields = ["timestamp", "unidade_med", "id_sensor"]

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ["id", "sensor", "ambiente", "timestamp", "valor"]
        read_only_fields = ["id", "timestamp"]

    def validate(self, data):
        sensor = data.get("sensor")
        if sensor and sensor.status == "inativo":
            raise serializers.ValidationError("Não foi possível realizar o registro de medição: Sensor inativo")
        return data
