from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home_view,name="home"),
    path('politics/',views.politics_view,name="politics"),
    path('transit/',views.last_news_transit_view,name="transit"),
    path('data/',views.last_news_data_view,name="data"),
    path('dollar-today/',views.economy_dollar_today_view,name="dollar_today"),
    path('field/',views.economy_field_view,name="field"),
    path('properties/',views.economy_properties_view,name="properties"),
    path('foregin-trade/',views.economy_foregin_trade_view,name="foregin_trade"),
    path('autos/',views.economy_autos_view,name="autos"),
    path('profit-calculator/',views.economy_profit_calculator_view,name="profit_calculator"),
    path('indices/',views.economy_indices_view,name="indices"),
    path('world/',views.the_world_view,name="world"),
    
    path('society/<society>/',views.society_views,name="society_common"),
    
    #path('community/',views.society_community_view,name="community"),
    path('community/<clicked>',views.society_community_sub_menu_common_view,name="community_common_menu"),
    path('community/everything/<clicked>',views.soicity_community_everything_view,name="community_common_menu_everything"),

    path('editorial/',views.opinion_editorial_view,name="editorial"),
    path('columnists/',views.opinion_columnists_view,name="columnists"),
    path('football/',views.sports_football_view,name="football"),
    path('statistics/',views.sports_statistics_view,name="statistics"),
    path('rugby/',views.sports_rugby_view,name="rugby"),
    path('tennis/',views.sports_tennis_view,name="tennis"),
    path('fashion/',views.lifestyle_fashion_view,name="fashion"),
    path('tourism/',views.lifestyle_tourism_view,name="tourism"),
    path('technology/',views.lifestyle_technology_view,name="technology"),
    path('holidays/',views.lifestyle_holidays_view,name="holidays"),
    path('podcasts/',views.lifestyle_podcasts_view,name="podcasts"),
    path('horoscope/',views.lifestyle_horoscope_view,name="horoscope"),
    path('horoscope/chineese',views.lifestyle_horoscope_chineese_view,name="chineese_horoscope"),
    path('shows/',views.shows_view,name="shows"),
    path('shows/<shows_id>',views.inside_shows_view,name="inside_shows"),
    path('magazine/',views.print_edition_magazine_view,name="magazine"),
    path('saturday/',views.print_edition_saturday_view,name="saturday"),
    path('ideas/',views.print_edition_ideas_view,name="ideas"),
    path('readers-letter/',views.print_edition_readers_letter_view,name="readers_letter"),
    path('humor/',views.print_edition_humor_view,name="humor"),
    path('awesome/',views.journal_awesome_view,name="awesome"),
    path('awesome/<parameter>/',views.awesome_sub_menus_view,name="awsome_sub_menu"),
    path('hi/',views.journal_hi_view,name="hi"),
    path('rolling-stone/',views.journal_rolling_stone_view,name="rolling_stone"),
    path('places/',views.journal_palces_view,name="places"),
    path('living/',views.journal_living_view,name="living"),
    path('brando/',views.journal_brando_view,name="brando"),
    path('yard/',views.journal_yard_view,name="yard"),
    
    path('article/',views.article_view,name="article"),
    path('author/',views.author_view,name="author"),
]
