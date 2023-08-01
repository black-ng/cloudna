from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello')


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


##  一些常用的返回数据操作
##  前后端不分离
def tpl(request):
    name = '斑比'
    list_demo = ['管路图', '哈哈', '是我啦0']
    dict_demo = {
        'name': 'hashiqi',
        'age': 'big',
        'sample': 'thouher',
    }
    mony_dict = [
        {
            'name': 'hashiqi',
            'age': 'big',
            'sample': 'thouher',
        },
        {
            'name': 'bigwu',
            'age': 'big',
            'sample': 'thouher',
        },
        {
            'name': 'bigduan',
            'age': 'big',
            'sample': 'thouher',
        }
    ]
    return render(request,
                  'tpl.html',
                  {
                      'n1': name,
                      'n2': list_demo,
                      'n3': dict_demo,
                      'n4': mony_dict,
                  }
                  )


#  获取联通中心新闻
def news(req):
    import requests

    url = 'http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news'
    result = requests.get(
        url=url,
        headers={'User-Agent': 'User-Agent'},
    )
    new_data = result.text
    print(new_data)

    return render(req, 'news.html', {'result_data': new_data})
