from django.urls import include, path

from coin import views

urlpatterns = [
    path('prices/', include([
        path('btc', views.CoinPriceView.as_view(), name='btc-price'),
    ])),
]
