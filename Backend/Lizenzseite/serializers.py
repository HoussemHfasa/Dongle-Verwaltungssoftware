from rest_framework import serializers
from .models import Lizenz


from rest_framework import serializers
from .models import Lizenz
from homepage.models import Dongle

class LizenzSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField()
    productcode = serializers.IntegerField()
    lizenzname = serializers.CharField(max_length=45)
    einheiten = serializers.IntegerField()
    gueltig_von = serializers.DateField()
    ablaufdatum = serializers.DateField()
    lizenzanzahl = serializers.IntegerField()
    mitarbeiter = serializers.CharField(max_length=45)
    projekt = serializers.CharField(max_length=45)
    dongle_lfd_nr_field = serializers.PrimaryKeyRelatedField(queryset=Dongle.objects.all())

    class Meta:
        model = Lizenz
        fields = '__all__'