from .models import Social

def ctx_dict(requets):
    dict_social={}
    urls=Social.objects.all()
    for url in urls:
        dict_social[url.key]=url.url
    return dict_social