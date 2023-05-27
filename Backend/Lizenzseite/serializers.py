from rest_framework import serializers
from .models import Lizenz


class LizenzSerializer(serializers.ModelSerializer):
    lfd_nr_field = serializers.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. The composite primary key (Lfd. Nr., Dognle_Lfd. Nr.) found, that is not supported. The first column is selected.
    productcode = serializers.IntegerField()  # Field name made lowercase.
    lizenzname = serializers.CharField( max_length=45)  # Field name made lowercase.
    einheiten = serializers.IntegerField()  # Field name made lowercase.
    gueltig_von = serializers.DateField()  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ablaufdatum = serializers.DateField()  # Field name made lowercase.
    lizenzanzahl = serializers.IntegerField()  # Field name made lowercase.
    mitarbeiter = serializers.CharField(max_length=45)  # Field name made lowercase.
    projekt = serializers.CharField(max_length=45)  # Field name made lowercase.
    dognle_lfd_nr_field = serializers.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        model = Lizenz
        fields = '__all__'