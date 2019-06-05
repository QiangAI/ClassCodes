from django.shortcuts import render


# Create your views here.
def map_data(request):
    context = {}
    context['data'] = '''[
                {name: '北京',value: 60},
                {name: '天津',value: 20},
                {name: '上海',value: 30},
                {name: '重庆',value: 40},
                {name: '四川',value: 60},
            ]'''
    return render(request, 'map/map.html', context)

#
# { % autoescape off %}
# {{post.content}}
# { % endautoescape %}
#
