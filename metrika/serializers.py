from .models import Statistics

from rest_framework import serializers


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('date', 'views', 'clicks', 'cost')


class StatisticsGetSerializes(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')

    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    def get_cpc(self, obj):
        try:
            return obj.cost / obj.clicks
        except TypeError:
            return "Not available"

    def get_cpm(self, obj):
        try:
            return obj.cost / obj.views * 1000
        except TypeError:
            return "Not available"
