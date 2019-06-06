from django.shortcuts import render


def mapdata(request):

    context ={}
    context['data']='''[
                    {
                        name:'北京',
                        value: 100,
                    },
                    {
                        name:'辽宁',
                        value:88,
                    },
                    {
                        name:'四川',
                        value:66
                    },
                    {
                        name:'山东',
                        value:34
                    },
                    {
                        name:'新疆',
                        value:18
                    },
                    {
                        name:'江苏',
                        value: 98
                    }
                ]'''
    print('访问')
    return render(request, 'biz/temp_map.html', context)