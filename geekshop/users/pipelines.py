from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse,urlencode

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from users.models import UserProfile



def save_user_profile(backend,user,response,*args,**kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about','photo_200')),
                                                access_token=response['access_token'],
                                                v='5.131')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    bdate = datetime.strptime(data['bdate'],'%d.%m.%Y').date()

    age = timezone.now().date().year - bdate.year
    user.age = age
    if age < 18:
        user.delete()
        raise  AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['photo_200']:
        photo_link = data['photo_200']
        photo_response = requests.get(photo_link)
        path_photo = f'users_image/{user.pk}.jpg'
        with open(f'media/{path_photo}','wb') as photo:
            photo.write(photo_response.content)
        user.image = path_photo
    user.save()