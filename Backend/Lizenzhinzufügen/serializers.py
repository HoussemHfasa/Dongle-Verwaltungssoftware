from rest_framework import serializers
from .models import Lizenz
from rest_framework import generics

# Der LizenzSerializer konvertiert das Lizenz-Modell in ein JSON-Format und umgekehrt.
class LizenzSerializer(serializers.ModelSerializer):
    # Die folgenden Zeilen definieren die Felder und deren Eigenschaften im Serializer.
    lfd_nr_field = serializers.IntegerField(required=False)
    firmcode = serializers.CharField()
    productcode = serializers.IntegerField()
    lizenzname = serializers.CharField(allow_blank=True)
    einheiten = serializers.IntegerField()
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    projekt = serializers.CharField()
    lizenzanzahl = serializers.IntegerField()
    mitarbeiter = serializers.CharField()
    dongle_serien_nr = serializers.CharField(required=False, allow_blank=True)
    kunde = serializers.CharField(required=False)

    class Meta:
        model = Lizenz
        fields = '__all__'

# DongleCreateView ist eine Klasse, die zum Erstellen eines neuen Dongles über eine API verwendet wird.
class DongleCreateView(generics.CreateAPIView):
    queryset = Lizenz.objects.all()
    serializer_class = LizenzSerializer
