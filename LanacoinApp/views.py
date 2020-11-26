from django.shortcuts import render
from datetime import date
import json
lst = [
    {
        'category': 'news',
        'title': ''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
        'topic': 'present',
        'date': 'october 14,2020',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'category': 'comment',
        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',
        'date': 'october 14,2020',
        'reporter': 'Diego Cabot',
        'pro_pic': 'images/3275561h134.jpg',
    },
    {
        'category': 'news',
        'title': ''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
        'topic': 'present',
        'date': 'october 14,2020',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'category': 'comment',
        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',
        'date': 'october 14,2020',
        'reporter': 'Diego Cabot',
        'pro_pic': 'images/3275561h134.jpg',
    },
    {
        'category': 'comment',
        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',
        'date': 'october 14,2020',
        'reporter': 'Diego Cabot',
        'pro_pic': 'images/3275561h134.jpg',
    },
]
more = [
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
]

lsst = [
    {

        'title': ''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
        'topic': 'present',
        'cover_pic': 'images/3275561h134.jpg',
        'reporter': 'By María Ayuso ',
        'date': 'October 31, 2020 '
    },
    {

        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',

        'cover_pic': 'images/3275561h134.jpg',
    },
    {

        'title': ''' The minimum wage will increase by 28%, far from the expectations of the unions ''',
        'topic': 'present',

        'cover_pic': 'images/3275561h134.jpg',
    },
    {

        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',

        'reporter': 'Diego Cabot',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {

        'title': ''' Argentina consecrates the myopia of Nodio observers  ''',
        'topic': 'present',

        'cover_pic': 'images/3275561h134.jpg',
    },
]
moore = [
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
    {
        'title': '''Argentina consecrates the myopia of Nodio observers''',
        'cover_pic': 'images/3275561h134.jpg',
    },
]
top_cards = [
    {
        'title': '''Coronavirus Cases on the rise or fall? The situation by party and commune throughout the country''',
        'topic': 'present',
        'cover_pic': 'images/H6PXHJEHNZCWPN7TQ2E4VMKWOE.jpg',
        'reporter': 'By María Ayuso ',
        'date': 'October 31, 2020 '
    },
    {
        'title': '''Mobility monitor: this is the movement of citizens since the beginning of the quarantine''',
        'topic': 'present',
        'cover_pic': 'images/ZQCDK4B7WBCGDL56BTR4ZVDP5Q.jpg',
        'reporter': 'By María Ayuso ',
        'date': 'October 31, 2020 '
    },
]


def home_view(request):
    top_news = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },

    ]
    top_news_lower = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },



    ]
    return render(request, 'home_page.html', {'top_news': top_news, 'top_news_lower': top_news_lower, 'more_news': top_news_lower, 'other_theme': top_news_lower, 'interest': top_news_lower, 'most_read': top_news_lower})

def latest_news_view(request):
    return render(request,'latest_news.html')
    
def article_view(request):
    today = date.today()
    d2 = today.strftime("%B %d")
    return render(request, 'post_inside.html', {'data': lst, 'more': more, 'date': d2})


def politics_view(request):

    return render(request, 'politics.html', {'data': lst, 'more': more})


def last_news_transit_view(request):

    return render(request, 'transit.html', {'data': lst, 'more': more})


def last_news_data_view(request):

    return render(request, 'data.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def economics_view(request):
    top_news = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },

    ]
    top_news_lower = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },

    ]

    return render(request, 'economics.html', {'top_news': top_news, 'top_news_lower': top_news_lower, 'more_news': top_news_lower, 'other_theme': top_news_lower, 'interest': top_news_lower, 'most_read': top_news_lower})


def economy_dollar_today_view(request):
    today = date.today()
    d2 = today.strftime("%B %d")
    return render(request, 'dollar_today.html', {'data': lst, 'more': more, 'date': d2})


def economy_field_view(request):
    return render(request, 'field.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def economy_properties_view(request):
    today = date.today()
    d2 = today.strftime("%B %d")
    return render(request, 'properties.html', {'data': lst, 'more': more, 'date': d2})


def economy_foregin_trade_view(request):
    today = date.today()
    d2 = today.strftime("%B %d")
    return render(request, 'foregin_trade.html', {'data': lst, 'more': more, 'date': d2})


def economy_autos_view(request):
    return render(request, 'autos.html', {'data': lst, 'more': more, })


def economy_profit_calculator_view(request):
    return render(request, 'profit_calculator.html', {'data': lst, 'more': more, })


def economy_indices_view(request):

    table_data = [
        {
            'table_name': 'Argentina Indices',

            'data1': [
                {
                    'company_name': 'Merval',
                    'country': 'argentina',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '-0.75%',
                    'date_time': '30.10 - 12:36',
                },
                {
                    'company_name': 'Merval',
                    'country': 'espana',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '0.00%',
                    'date_time': '30.10 - 12:36',
                },
                {
                    'company_name': 'Merval',
                    'country': 'espana',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '0.75%',
                    'date_time': '30.10 - 12:36',
                }
            ]
        },
        {
            'table_name': 'Europe Indices',

            'data1': [
                {
                    'company_name': 'Merval',
                    'country': 'argentina',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '-0.75%',
                    'date_time': '30.10 - 12:36',
                },
                {
                    'company_name': 'Merval',
                    'country': 'espana',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '0.00%',
                    'date_time': '30.10 - 12:36',
                },
                {
                    'company_name': 'Merval',
                    'country': 'espana',
                    'last': '1415554552',
                    'previous': '445255414',
                    'variation': '0.75%',
                    'date_time': '30.10 - 12:36',
                }
            ]
        },
    ]

    return render(request, 'indices.html', {'data': table_data})


def the_world_view(request):
    return render(request, 'world.html', {'data': lst, 'more': more, })


def society_views(request, society):
    page_info = {}
    if society == "buenos_aires":
        page_info = {
            'page_title': 'Latest news from Buenos Aires - LA NACION',
            'sub_link': 'Buenos Aires',
            'main_title': 'Buenos Aires',
            'view_more': 'SEE MORE NOTES FROM  Buenos Aires',
        }
    elif society == "security":
        page_info = {
            'page_title': 'Latest news on Security  - LA NACION',
            'sub_link': 'Security',
            'main_title': 'Security',
            'view_more': 'SEE MORE NOTES FROM  Security ',
        }
    elif society == "education":
        page_info = {
            'page_title': 'Latest news on Education  - LA NACION ',
            'sub_link': 'Education',
            'main_title': 'Education',
            'view_more': 'SEE MORE NOTES FROM  Education',
        }
    elif society == "culture":
        page_info = {
            'page_title': 'Latest news from Culture  - LA NACION',
            'sub_link': 'Culture',
            'main_title': 'Culture',
            'view_more': 'SEE MORE NOTES FROM Culture',
        }
    elif society == "health":
        page_info = {
            'page_title': 'Latest health news - LA NACION',
            'sub_link': 'Health',
            'main_title': 'Health',
            'view_more': 'SEE MORE health NOTES',
        }
    elif society == "science":
        page_info = {
            'page_title': 'Latest science news - LA NACION',
            'sub_link': 'Science',
            'main_title': 'Science',
            'view_more': 'SEE MORE science NOTES',
        }
    elif society == "community":
        return render(request, 'community.html', {'data': lsst, 'more': moore, 'cards': top_cards})

    return render(request, 'society_common.html', {'pg_info': page_info, 'data': lst, 'more': more})


def society_community_sub_menu_common_view(request, clicked):
    page_info = {}
    if clicked == "discrimination":
        page_info = {
            'page_title': 'Latest news on Discrimination  - LA NACION',
            'sub_link': 'Discrimination ',
            'main_title': 'Discrimination ',
            'view_more': 'SEE MORE NOTES on Discrimination ',
        }
    elif clicked == "diversity":
        page_info = {
            'page_title': 'Diversity - LA NACION',
            'sub_link': 'Diversity',
            'main_title': 'Diversity',
            'view_more': 'SEE MORE From Diversity',
        }
        return render(request, 'community_diversity.html', {'pg_info': page_info, 'data': lsst, 'more': moore, })
    elif clicked == "addictions":
        page_info = {
            'page_title': 'Latest Addictions  news - LA NACION',
            'sub_link': 'Addictions ',
            'main_title': 'Addictions ',
            'view_more': 'SEE MORE Addictions  NOTES',
        }
    elif clicked == "human_rights":
        page_info = {
            'page_title': 'Latest news on Human rights   - LA NACION',
            'sub_link': 'Human rights  ',
            'main_title': 'Human rights  ',
            'view_more': 'SEE MORE NOTES on Human rights  ',
        }
    elif clicked == "grooming":
        page_info = {
            'page_title': 'Latest Grooming  news - LA NACION',
            'sub_link': 'Grooming ',
            'main_title': 'Grooming ',
            'view_more': 'SEE MORE Grooming  NOTES',
        }
    elif clicked == "sexual_abuse":
        page_info = {
            'page_title': 'Latest news on Sexual abuse   - LA NACION',
            'sub_link': 'Sexual abuse  ',
            'main_title': 'Sexual abuse  ',
            'view_more': 'SEE MORE NOTES on Sexual abuse  ',
        }

    elif clicked == "proverty":
        page_info = {
            'page_title': 'Latest Poverty   news - LA NACION',
            'sub_link': 'Poverty  ',
            'main_title': 'Poverty  ',
            'view_more': 'SEE MORE Poverty   NOTES',
        }

    elif clicked == "alcohol":
        page_info = {
            'page_title': 'Latest alcohol   news - LA NACION',
            'sub_link': 'alcohol  ',
            'main_title': 'alcohol  ',
            'view_more': 'SEE MORE alcohol   NOTES',
        }

    elif clicked == "teenagers":
        page_info = {
            'page_title': 'Latest news form Teenagers  - LA NACION',
            'sub_link': 'Teenagers ',
            'main_title': 'Teenagers ',
            'view_more': 'SEE MORE NOTES from Teenagers ',
        }

    elif clicked == "gender_identity":
        page_info = {
            'page_title': 'Latest news on DGender identity  - LA NACION',
            'sub_link': 'Gender identity  ',
            'main_title': 'Gender identity  ',
            'view_more': 'SEE MORE NOTES on Gender identity  ',
        }
    elif clicked == "racism":
        page_info = {
            'page_title': 'Racism - LA NACION',
            'sub_link': 'Racism',
            'main_title': 'Racism',
            'view_more': 'SEE MORE From Racism',
        }
        return render(request, 'community_diversity.html', {'pg_info': page_info, 'data': lsst, 'more': moore, })

    elif clicked == "hunger":
        page_info = {
            'page_title': 'Hunger for the future  - LA NACION',
            'sub_link': 'Hunger for the future ',
            'main_title': 'Hunger for the future ',
            'view_more': 'SEE MORE From Hunger for the future ',
        }
        return render(request, 'hunger.html', {'pg_info': page_info, 'data': lsst, 'more': moore, 'cards': top_cards})
    elif clicked == "everything":
        return render(request, 'community_everything.html')
    return render(request, 'community_common.html', {'pg_info': page_info, 'data': lst, 'more': more})


def soicity_community_everything_view(request, clicked):
    page_info = {}
    if clicked == "abuse":
        page_info = {
            'page_title': 'Abuse - LA NACION',
            'sub_link': 'Abuse ',
            'view_more': '',
            'bg_color': '#68495B',
            'img': 'images/APIPVKRKCVAEFPB4T7KGHF3WHA.png',
        }
    elif clicked == "gender":
        page_info = {
            'page_title': 'Gender violence  - LA NACION',
            'sub_link': 'Gender violence ',
            'view_more': '',
            'bg_color': '#7A303D',
            'img': 'images/OJOZPIPTIZGZ5C7POZOUX3P3MA.png',
        }
    elif clicked == "education":
        page_info = {
            'page_title': 'Inclusive education - LA NACION',
            'sub_link': 'Inclusive education',
            'view_more': '',
            'bg_color': '#5F837F',
            'img': 'images/LTWPACQGNRHZ5PHHY4Q2FIAXGE.png',
        }
    elif clicked == "bullying":
        page_info = {
            'page_title': 'Bullying - LA NACION',
            'sub_link': 'Bullying ',
            'view_more': '',
            'bg_color': '#EE6052',
            'img': 'images/IDNN52OVMVDCJEELASPPZ7PHYA.png',
        }
    elif clicked == "eating":
        page_info = {
            'page_title': 'Eating disorders - LA NACION',
            'sub_link': 'Eating disorders ',
            'view_more': '',
            'bg_color': '#6092CD',
            'img': 'images/T33ULSBBWRA6DHW6IIIZKKZVUY.png',
        }
    elif clicked == "addictions":
        page_info = {
            'page_title': 'Addictions   - LA NACION',
            'sub_link': 'Addictions  ',
            'view_more': '',
            'bg_color': '#8F828B',
            'img': 'images/CFF6RLAZ7FBRBPLN3U5P4QT3YA.png',
        }
    return render(request, 'common_lets_talk.html', {'pg_info': page_info, 'data': lsst, 'more': moore, 'cards': top_cards})


def opinion_editorial_view(request):
    return render(request, 'editorial.html', {'data': lst, 'more': more, })


def opinion_columnists_view(request):
    columnists = [
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
        {
            'name': 'Joaquín Morales Solá',
            'pro_pic': 'images/3207350w90.webp',
        },
    ]
    return render(request, 'columnists.html', {'data': columnists, })

def sports_view(request):
    top_news = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },

    ]
    top_news_lower = [
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Land grab.',
            'sub_title': "Strong march in Entre Ríos after Etchevehere's complaint",
            'details': '''Producers from the province are mobilized in Santa Elena, in front of the former official's field; they went there to reject the usurpation''',
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/recent-1.webp'
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },
        {
            'title': 'Massive and mandatory. ',
            'sub_title': "The vaccination plan that the Government plans at the end of the year",
            'reporter': 'By Jaime Rosemberg',
            'cover_photo': 'images/3449885h186.webp',
        },



    ]
    return render(request, 'sports.html', {'top_news': top_news, 'top_news_lower': top_news_lower, 'more_news': top_news_lower, 'other_theme': top_news_lower, 'interest': top_news_lower, 'most_read': top_news_lower})

def sports_football_view(request):
    return render(request, 'football.html', {'data': lst, 'more': more, })


def sports_statistics_view(request):
    sp_data = [
        {
            'table_id': '1',
            'table_title': 'GROUP A',
            'last_col_name': 'Recent Results',

            'tbody':
            [
                {
                    'Pos': 1,
                    'Flag': 'images/Paris Saint Germain.png',
                    'Name': 'Paris Saint Germain',
                    'Pts': 14,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 3,
                    'DG': 15,
                    'recent_result': [
                        {
                            'date': 'Wednesday 4th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 15th October 2020',
                            'result': 'Won',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 10th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 20th October 2020',
                            'result': 'Tie',
                            'vs': '3-0 vs FCB'
                        },
                    ]
                },

                {
                    'Pos': 2,
                    'Flag': 'images/Real Madrid .png',
                    'Name': 'Real Madrid ',
                    'Pts': 15,
                    'PJ': 6,
                    'G': 8,
                    'E': 1,
                    'P': 4,
                    'DG': 15,
                    'recent_result': [
                        {
                            'date': 'Wednesday 1th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 30th October 2020',
                            'result': 'Won',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 14th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 11th October 2020',
                            'result': 'Tie',
                            'vs': '3-0 vs FCB'
                        },
                    ]

                },
                {
                    'Pos': 3,
                    'Flag': 'images/Club Brugge.png',
                    'Name': 'Club Brugge ',
                    'Pts': 12,
                    'PJ': 6,
                    'G': 5,
                    'E': 1,
                    'P': 2,
                    'DG': 15,
                    'recent_result': [
                        {
                            'date': 'Wednesday 6th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 5th October 2020',
                            'result': 'Won',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 7th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 8th October 2020',
                            'result': 'Tie',
                            'vs': '3-0 vs FCB'
                        },
                    ]
                },
                {
                    'Pos': 4,
                    'Flag': 'images/Galatasaray.png',
                    'Name': 'Galatasaray ',
                    'Pts': 10,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 1,
                    'DG': 15,
                    'recent_result': [
                        {
                            'date': 'Wednesday 1th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 2th October 2020',
                            'result': 'Won',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 3th October 2020',
                            'result': 'Lost',
                            'vs': '3-0 vs FCB'
                        },
                        {
                            'date': 'Wednesday 4th October 2020',
                            'result': 'Tie',
                            'vs': '3-0 vs FCB'
                        },
                    ]
                },
            ]
        },
        {
            'table_id': '2',
            'table_title': 'GROUP B',
            'last_col_name': 'Pr.',

            'tbody': [
                {
                    'Pos': 1,
                    'Flag': 'images/Paris Saint Germain.png',
                    'Name': 'Paris Saint Germain',
                    'Pts': 14,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 3,
                    'DG': 15,
                    'Pr': 14,
                },

                {
                    'Pos': 2,
                    'Flag': 'images/Real Madrid .png',
                    'Name': 'Real Madrid ',
                    'Pts': 15,
                    'PJ': 6,
                    'G': 8,
                    'E': 1,
                    'P': 4,
                    'DG': 15,
                    'Pr': 12,
                },
                {
                    'Pos': 3,
                    'Flag': 'images/Club Brugge.png',
                    'Name': 'Club Brugge ',
                    'Pts': 12,
                    'PJ': 6,
                    'G': 5,
                    'E': 1,
                    'P': 2,
                    'DG': 15,
                    'Pr': 20,
                },
                {
                    'Pos': 4,
                    'Flag': 'images/Galatasaray.png',
                    'Name': 'Galatasaray ',
                    'Pts': 10,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 1,
                    'DG': 15,
                    'Pr': 10,
                },
            ]
        },

        {
            'table_id': '3',
            'table_title': 'GROUP C',
            'last_col_name': 'Pr.',

            'tbody': [
                {
                    'Pos': 1,
                    'Flag': 'images/Paris Saint Germain.png',
                    'Name': 'Paris Saint Germain',
                    'Pts': 14,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 3,
                    'DG': 15,
                    'Pr': 14,
                },

                {
                    'Pos': 2,
                    'Flag': 'images/Real Madrid .png',
                    'Name': 'Real Madrid ',
                    'Pts': 15,
                    'PJ': 6,
                    'G': 8,
                    'E': 1,
                    'P': 4,
                    'DG': 15,
                    'Pr': 12,
                },
                {
                    'Pos': 3,
                    'Flag': 'images/Club Brugge.png',
                    'Name': 'Club Brugge ',
                    'Pts': 12,
                    'PJ': 6,
                    'G': 5,
                    'E': 1,
                    'P': 2,
                    'DG': 15,
                    'Pr': 20,
                },
                {
                    'Pos': 4,
                    'Flag': 'images/Galatasaray.png',
                    'Name': 'Galatasaray ',
                    'Pts': 10,
                    'PJ': 6,
                    'G': 2,
                    'E': 1,
                    'P': 1,
                    'DG': 15,
                    'Pr': 10,
                },
            ]
        },

    ]
    return render(request, 'statistics.html', {'data': sp_data, })


def sports_rugby_view(request):
    return render(request, 'rugby.html', {'data': lst, 'more': more, })


def sports_tennis_view(request):
    return render(request, 'tennis.html', {'data': lst, 'more': more, })


def lifestyle_fashion_view(request):
    return render(request, 'fashion.html', {'data': lst, 'more': more, 'cards': top_cards})


def lifestyle_tourism_view(request):
    return render(request, 'tourism.html', {'data': lst, 'more': more})


def lifestyle_technology_view(request):
    return render(request, 'technology.html', {'data': lsst, 'more': moore})


def lifestyle_holidays_view(request):
    return render(request, 'holidays.html')


def lifestyle_podcasts_view(request):
    return render(request, 'podcast.html')


def lifestyle_horoscope_view(request):
    signs = [
        {
            # the first letter must be capital and others small in sign key
            'sign': 'Aries',
            'bd': '21/3 al 20/4',
            'des': '''After so long, you can develop your creative vision as long as what you want is strong enough. Don't limit yourself. ''',

        },
        {
            'sign': 'Taurus',
            'bd': '21/4 al 21/5 ',
            'des': '''If you feel internally dissatisfied, know that you should focus on planning a new life project that makes you feel even more gratified. '''
        }
    ]
    return render(request, 'horoscope_zodiac.html', {'data': signs})


def lifestyle_horoscope_inside_view(request, value):
    details = {}

    if value == "Aries":
        details = {
            'title': '♈ ARIES horoscope today - LA NACION ',
            'sign': 'Aries',
            'name': 'Renata Dossi',
            'bd': '21/3 al 20/4',
            'des': '''Know that if you adopt a more tolerant attitude towards your family, you can better guide your life. Listen to the complaints and spend more time with them. ''',
            'love': '''
    If you feel that your soul mate is not giving you what you want or need, find a new way to love. Tell him about the fears and emotions you are experiencing.''',
            'wealth': '''
    These days, you will have a strong power of persuasion in front of your co-workers. Do not hesitate and use it as soon as possible in your work environment. ''',
            'wellness': '''Try to take your time if you find yourself nervous or overwhelmed by the situations you are experiencing. Oxygenate your lungs and relax.''',
            'for': 'Kiron ',
            'week_love': '''
    If you feel that your soul mate is not giving you what you want or need, find a new way to love. Tell him about the fears and emotions you are experiencing.''',
            'money': '''
    These days, you will have a strong power of persuasion in front of your co-workers. Do not hesitate and use it as soon as possible in your work environment. ''',
            'key': '''Try to take your time if you find yourself nervous or overwhelmed by the situations you are experiencing. Oxygenate your lungs and relax.''',

        }
    return render(request, 'horoscope_zodiac_inside.html', {'x': details})


def lifestyle_horoscope_chineese_view(request):
    animal = [
        {
            # the first letter must be capital and others small in sign key
            'animal': 'Rat',
            'years': '1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009. ',


        },
        {
            'animal': 'Buffalo',
            'years': '1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009. ',

        }
    ]
    return render(request, 'horoscope_chinese.html', {'data': animal})


def lifestyle_horoscope_chineese_inside_view(request, value):
    details = {}
    if value == 'Rat':
        details = {
            'animal': 'Rat',
            'years': '1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020. ',
            'this_year': '''In the year of your sign, you will know how to enhance all your talents to obtain what you want most. With a more practical and determined attitude, you will feel that nothing is out of your reach. You will know how to manage your hyperactivity with intelligence and you will have the possibility of meeting influential people who will benefit you in your profession and in the businesses you do. It is a time of concretions, a very productive year where you will notice that luck is on your side. Thanks to your creativity and professionalism, the most complicated things will be easy to do. The challenge will be knowing how to accept the good advice of more experienced people and learn to delegate when situations overwhelm you. In love, do not be afraid to make decisions, trust your experience and follow what your heart dictates. ''',
            'character': '''Admired and honored for its sagacity and skill, in the East the Rat is a symbol of luck and prosperity. Charming creature capable of captivating anyone, she is aware of this quality and likes to flaunt her style. Curious, she is always on the hunt for new information, has a great sense of humor and lives in constant movement. Despite being very sociable, you need to spend time alone, to think, meditate, and get inspired. Very focused on herself, it is difficult for her to see beyond, however, she is usually very protective and generous with those who are faithful to her. Intelligent, restless and impatient, she always achieves her goals, knows how to find the fastest way and nothing stops her. Like the Sagittarius woman, the Rat adores her family, is passionate and difficult to tame, she does not like being wanted to handle or betrayed. You need a lot of affection to value yourself, because you have a tendency to underestimate yourself. This sign is analogous, that is, with similar characteristics, to the Sagittarius sign. ''',
        }

    return render(request, 'horoscope_chinese_inside.html', {'x': details})


def shows_view(request):
    movies = [
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }, {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }
    ]
    next_movies = [
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
            'release': '20.10.2020'
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }, {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }
    ]
    return render(request, 'shows.html', {'data': movies, 'next': next_movies})


def inside_shows_view(request, shows_id):
    next_movies = [
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
            'release': '20.10.2020'
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }, {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }
    ]
    movies_details = {
        'id': "1",
        'poster': "images/imagen-placeholder-cine.png",
        'title': 'Childish',
        'in_out_comming': 'in',
        'Premiere': '24.10.2020',
        'Actor': 'Flopy Tesouro, Cristina Maresca, Rodrigo Noya',
        'Address': 'Diego Rinaldi',
        'Music': 'Mauro Garcia Barbe',
        'Choreography': 'Ignacio Saraceni',
        'detail': '''Synopsis of The Compass of Dreams: Carolo misses the talks with her grandfather, Lucia dreams of being a singer but her shyness prevents her from doing so. Together they set out on the road to the Haunted House where a curious character will help them discover surprising things, love for grown-ups and trust in dreams. ''',
        'genere': 'Comedy',
        'Address': 'San Nicolás - Autonomous City of Buenos Aires ',
        'billboard': 'Theater',
    }
    next_movies = [
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
            'release': '20.10.2020'
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        },
        {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }, {
            'cover_pic': 'images/imagen-placeholder-cine.png',
            'title': 'An abominable friend ',
            'theater': 'Comafi Multitheater',
        }
    ]

    return render(request, 'inside_shows.html', {'movie': movies_details, 'this_theater': next_movies})


def print_edition_magazine_view(request):
    return render(request, 'magazine.html', {'data': lst, 'more': more})


def print_edition_saturday_view(request):
    return render(request, 'saturday.html', {'data': lst, 'more': more})


def print_edition_ideas_view(request):
    return render(request, 'ideas.html', {'data': lst, 'more': more})


def print_edition_readers_letter_view(request):
    return render(request, 'readers_letter.html', {'data': lst, 'more': more})


def print_edition_humor_view(request):
    joke = [
        {
            'title': 'Gaturro',
            'author': 'by Liniers ',
            'img1': 'images/3275561h134.jpg',
            'img2': 'images/3275561h134.jpg',

        },
        {
            'title': 'Gaturro',
            'author': 'by Liniers ',
            'img1': 'images/3275561h134.jpg',
            'img2': '',

        },
        {
            'title': 'Gaturro',
            'author': 'by Liniers ',
            'img1': '',
            'img2': 'images/3275561h134.jpg',

        },
    ]
    personal_data = {
        'nick_name': 'Nik',
        'name': 'Cristian The bell',
        'pro_pic': 'images/3275561h134.jpg',
        'bio': '''WHO IS NIK?

                    Cristian Dzwonik, Nik, was born in Buenos Aires 49 years ago. He is a graduate of the National College of Buenos Aires and a Graphic Designer received from the UBA. He also completed studies in advertising, computer graphics and digital photomontage.

                    From the age of 12 he studied at the Carlos Garaycochea drawing school and began to work regularly as a graphic humorist at the age of 17 in Muy Interesante magazine. His first cartoons of political humor were published in the newspaper El Cronista Comercial. At 22 he joined LA NACION and since then he has worked as a current graphic humorist in various sections.

                    Since October 1992 the political joke of the main body accompanies the daily readers of the newspaper. In April 1994, "La Foto que Habla" began to be published. Around the same time, Nik's humor reaches La Revista del Domingo, a page that received numerous international awards.

                    In 1996 Gaturro, Agatha, Gaturrin, Mamurra, Gatulongo and the whole feline family took shape in the daily strip of the Last Page of LA NACION. From there, the elusive pussycat walks through the office, tries to win over his "amigovia" Agatha, tries to study "Brutish English" at school or educates his nephew Gaturrín.

                    Gaturro's strip already reaps a legion of fans of all ages and from various countries, thanks to the internet.

                    At the beginning of 1997, LANACION.com added Nik's humorous page to its edition, where you can find all the jokes from the newspaper, wallpapers and unpublished drawings.
                Cristian Dzwonik, Nik, was born in Buenos Aires 49 years ago. He is a graduate of the National College of Buenos Aires and a Graphic Designer received from the UBA. He also completed studies in advertising, computer graphics and digital photomontage.

                    From the age of 12 he studied at the Carlos Garaycochea drawing school and began to work regularly as a graphic humorist at the age of 17 in Muy Interesante magazine. His first cartoons of political humor were published in the newspaper El Cronista Comercial. At 22 he joined LA NACION and since then he has worked as a current graphic humorist in various sections.

                    Since October 1992 the political joke of the main body accompanies the daily readers of the newspaper. In April 1994, "La Foto que Habla" began to be published. Around the same time, Nik's humor reaches La Revista del Domingo, a page that received numerous international awards.

                    In 1996 Gaturro, Agatha, Gaturrin, Mamurra, Gatulongo and the whole feline family took shape in the daily strip of the Last Page of LA NACION. From there, the elusive pussycat walks through the office, tries to win over his "amigovia" Agatha, tries to study "Brutish English" at school or educates his nephew Gaturrín.

                    Gaturro's strip already reaps a legion of fans of all ages and from various countries, thanks to the internet.

                    At the beginning of 1997, LANACION.com added Nik's humorous page to its edition
        ''',
    }
    return render(request, 'humor.html', {'jokes': joke, 'data': personal_data})


def author_view(request):
    personal_data = {
        'name': 'Joaquin Morales Solá',
        'pro_pic': 'images/3275561h134.jpg',
        'bio': '''He has practiced journalism since he was 16 years old when he joined the newspaper 
        La Gaceta de Tucumán. In 1975, Clarín summoned him to be deputy secretary of the Political section. 
        For 12 years he was second editor in chief and author of the Sunday political column of that 
        newspaper. He was a political columnist for the Telefé newscast and Bernardo Neustadt's 
        "Tiempo Nuevo" program. During 1997, he hosted "Dos en la noticias" together with Magdalena 
        Ruiz Guiñazú, on the former Channel 9. Currently, he is a political columnist for the newspaper 
        LA NACION. In 1990, the Italian government awarded him the Order of Merit of the Italian Republic. 
        Later, in 1992, Spain distinguished him with the Order of Isabel la Católica. In 1998, he received 
        the National Order of Merit awarded by the Republic of France. In his latest book, "Sin excusas" 
        (South American), Morales Solá reveals dialogues with former vice president Chacho Alvarez, about 
        the secret plot of bribery in the Senate,
        the causes of his resignation and the errors that led to the failure of the Alliance . ''',
    }
    return render(request, 'post_inside_info.html', {'bio_data': personal_data, 'data': lst, 'more': more})


def journal_awesome_view(request):
    return render(request, 'awesome.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_hi_view(request):
    return render(request, 'hi.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_rolling_stone_view(request):
    return render(request, 'rolling_stone.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_palces_view(request):
    return render(request, 'places.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_living_view(request):
    return render(request, 'living.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_brando_view(request):
    return render(request, 'brand.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def journal_yard_view(request):
    return render(request, 'yard.html', {'data': lsst, 'more': moore, 'cards': top_cards})


def awesome_sub_menus_view(request, parameter):
    page_info = {}
    if parameter == "healthy_kitchen":
        page_info = {
            'page_title': 'Latest news from Healthy Kitchen - LA NACION',
            'sub_link': 'Healthy kitchen',
            'main_title': 'Healthy kitchen',
            'view_more': 'SEE MORE NOTES FROM Healthy Kitchen',
        }
    elif parameter == "travels":
        page_info = {
            'page_title': 'Latest news from OHLALÁ! Travels - LA NACION',
            'sub_link': 'OHLALÁ! Travels',
            'main_title': 'OHLALÁ! Travels',
            'view_more': 'SEE MORE NOTES FROM OHLALÁ! Travels',
        }
    elif parameter == "makers":
        page_info = {
            'page_title': 'Latest news from  OHLALÁ! makers  - LA NACION',
            'sub_link': ' OHLALÁ! makers ',
            'main_title': ' OHLALÁ! makers ',
            'view_more': 'SEE MORE NOTES FROM  OHLALÁ! makers ',
        }
    elif parameter == "factory":
        page_info = {
            'page_title': 'Latest news from OHLALÁ Factory  - LA NACION',
            'sub_link': 'OHLALÁ Factory ',
            'main_title': 'OHLALÁ Factory ',
            'view_more': 'SEE MORE NOTES FROM OHLALÁ Factory ',
        }
    elif parameter == "fest":
        page_info = {
            'page_title': 'Latest news from OH DEAR! Fest  - LA NACION',
            'sub_link': 'OH DEAR! Fest ',
            'main_title': 'OH DEAR! Fest ',
            'view_more': 'SEE MORE NOTES FROM OH DEAR! Fest ',
        }

    return render(request, 'community_common.html', {'pg_info': page_info, 'data': lst, 'more': more})


def all_common_side_view(request, parameter):
    page_info = {}
    if parameter == 'lifestyle':
        page_info = {
            'page_title': 'Latest News from Lifestyle- LA NACION',
            'sub_link': 'Lifestyle',
            'view_more': 'See more Lifestyle notes',
            'main_title': 'Lifestyle',
        }
    elif parameter == 'society':
        page_info = {
            'page_title': 'Latest News from Society- LA NACION',
            'sub_link': 'Society',
            'view_more': 'See more Society notes',
            'main_title': 'Society',
        }
    elif parameter == 'opinion':
        page_info = {
            'page_title': 'Latest Opinion News- LA NACION',
            'sub_link': 'Opinion',
            'view_more': 'See more Opinion notes',
            'main_title': 'Opinion',
        }
    elif parameter == 'shows_main':
        page_info = {
            'page_title': 'Latest News From Shows - LA NACION',
            'sub_link': 'Shows ',
            'view_more': 'See more notes from Shows ',
            'main_title': 'Shows ',
        }
        return render(request, 'common_side_two.html', {'data': lst, 'more': moore, 'cards': top_cards, 'pg_info': page_info})
    elif parameter == 'entrepreneurs':
        page_info = {
            'page_title': 'Latest Entrepreneurs News - LA NACION',
            'sub_link': 'Entrepreneurs',
            'view_more': 'See more notes from Entrepreneurs',
            'main_title': 'Entrepreneurs',
        }
    return render(request, 'common_side_nav.html', {'data': lst, 'more': more, 'pg_info': page_info})
