from rest_framework import serializers
from .models import Lizenz
from rest_framework import generics


class LizenzSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField(required=False)  # Anpassung: Das Feld ist optional
    firmcode = serializers.CharField()
    productcode = serializers.IntegerField() 
    lizenzname = serializers.CharField(allow_blank=True)
    Einheiten = serializers.IntegerField() 
    gueltig_von = serializers.DateField()
    gueltig_bis = serializers.DateField()
    projekt = serializers.CharField()
    lizenzanzahl = serializers.IntegerField() 
    mitarbeiter= serializers.CharField()
    dongle_serien_nr = serializers.CharField()
    kunde=serializers.CharField()

    # Füge das kunde-Feld hinzu
    class Meta:
        model = Lizenz
        fields = '__all__'

# View
class DongleCreateView(generics.CreateAPIView):
    queryset = Lizenz.objects.all()
    serializer_class = LizenzSerializer
