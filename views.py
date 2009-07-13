from django.http import HttpResponse



def display_meta(request): 
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def hello(request):
      return HttpResponse("Hello world-------->> this is test # 1")
