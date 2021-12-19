from django.db.models import Q
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from .models import Statistics
from .serializers import StatisticsSerializer, StatisticsGetSerializes


class StatisticsListView(ListAPIView):
    serializer_class = StatisticsGetSerializes

    def get(self, request, *args, **kwargs):
        sort_param = self.request.query_params.get('sort')
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True).data
        if sort_param:
            is_reversed = False
            if '-' in sort_param:
                sort_param = sort_param.replace('-', '')
                is_reversed = True
            serializer = sorted(serializer, key=lambda k: k[sort_param], reverse=is_reversed)

        return Response(serializer)

    def get_queryset(self):
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        lookup = Q(is_deleted=False)
        if from_date:
            lookup = lookup | Q(date__gte=from_date)
        if to_date:
            lookup = lookup | Q(date__lte=to_date)

        queryset = Statistics.objects.filter(lookup)
        return queryset


class StatisticsCreateView(CreateAPIView):
    serializer_class = StatisticsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class StatisticsResetView(DestroyAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

    def delete(self, request, *args, **kwargs):
        qs = self.get_queryset()
        for stat in qs:
            stat.is_deleted = True
            stat.save()
        return Response({"Message": "Statistics Reset"}, status.HTTP_200_OK)
