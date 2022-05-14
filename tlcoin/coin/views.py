from datetime import datetime

from django.shortcuts import render
from rest_framework import generics

from .serializers import CoinPriceSerializer


class CoinPriceView(generics.ListAPIView):
    '''
    View for filtering Cryptocurrency price on date
    '''
    serializer_class = CoinPriceSerializer
    model = serializer_class.Meta.model
    paginate_by = 100

    def get_queryset(self):
        query_date = self.request.query_params.get('date')
        date_obj = datetime.strptime(query_date, '%d-%m-%Y') if query_date else datetime.today()
        queryset = self.model.objects.filter(price_updated_at__date=date_obj)
        return queryset
