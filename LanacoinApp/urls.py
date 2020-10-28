from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home_view,name="home"),
    path('politics/',views.politics_view,name="politics"),
    path('transit/',views.last_news_transit_view,name="transit"),
    path('data/',views.last_news_data_view,name="data"),
    path('dollar-today/',views.economy_dollar_today_view,name="dollar_today"),
    path('properties/',views.economy_properties_view,name="properties"),
    path('foregin-trade/',views.economy_foregin_trade_view,name="foregin_trade"),
    path('autos/',views.economy_autos_view,name="autos"),
    path('world/',views.the_world_view,name="world"),
    path('article/',views.article_view,name="article"),
]
