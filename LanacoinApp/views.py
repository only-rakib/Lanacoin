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


def sports_football_view(request):
    return render(request, 'football.html', {'data': lst, 'more': more, })


def sports_statistics_view(request):
    sp_data = [
        {
            'table_id':'1',
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
            'table_id':'2',
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
            'table_id':'3',
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
