from django.shortcuts import render
from datetime import date

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
        'cover_pic': 'images/3358974h407.webp',
    },
    {
        'title': '''Mobility monitor: this is the movement of citizens since the beginning of the quarantine''',
        'topic': 'present',
        'cover_pic': 'images/3359066h407.gif',
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


def society_buenos_aires_view(request):
    return render(request, 'buenos_aires.html', {'data': lst, 'more': more, })


def society_security_view(request):
    return render(request, 'security.html', {'data': lst, 'more': more, })


def society_education_view(request):
    return render(request, 'education.html', {'data': lst, 'more': more, })


def society_culture_view(request):
    return render(request, 'culture.html', {'data': lst, 'more': more, })


def society_health_view(request):
    return render(request, 'health.html', {'data': lst, 'more': more, })


def society_science_view(request):
    return render(request, 'science.html', {'data': lst, 'more': more, })


def opinion_editorial_view(request):
    return render(request, 'editorial.html', {'data': lst, 'more': more, })

def opinion_columnists_view(request):
    columnists=[
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
        {
            'name':'Joaquín Morales Solá',
            'pro_pic':'images/3207350w90.webp',
        },
    ]
    return render(request, 'columnists.html', {'data':columnists,})


def sports_football_view(request):
    return render(request, 'football.html', {'data': lst, 'more': more, })


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


def print_edition_magazine_view(request):
    return render(request, 'magazine.html', {'data': lst, 'more': more})


def print_edition_saturday_view(request):
    return render(request, 'saturday.html', {'data': lst, 'more': more})


def print_edition_ideas_view(request):
    return render(request, 'ideas.html', {'data': lst, 'more': more})


def print_edition_readers_letter_view(request):
    return render(request, 'readers_letter.html', {'data': lst, 'more': more})
