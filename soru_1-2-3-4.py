import requests
from typing import Callable, Generator

def error_handler(func: Callable) -> Callable:
    '''
    Fonksiyonun(func) tipi Callable tipinde (yani cagiralabilir oldugunu fonksiyon oldugunu anlayabiliriz) olmasi
    uygundur. Ancak farkli tipte de iletilebilinir.
    :param: func
    :return: func
    '''
    def wrapper(*args, **kwargs) -> dict:
        '''
        Fonksiyondan gelen degerin status_code degeri 200 yada ok ise gelen degeri Json'a cast et ve result degerini dondur
        :return: dict tipinde donecektir, ancak farkli bir gonderimde yapilabilinir. Python tarafindan kontrolu yok.
        '''
        results = None
        response = func(*args, **kwargs)
        if response.ok:
            response = response.json()
            results = response.get('results')
        return results

    return wrapper


def converter(func: Callable) -> Callable:  #  Bu decorator Calleble(func) tipinde girdi alir ve dict tipinde cikti
    # yapmasi makbuldur. Decorator list'e cast etmektedir. Donen sonuc list tipinde olacaktir.
    def wrapper(*args, **kwargs) -> dict:
        response = func(*args, **kwargs)
        return list(response)

    return wrapper


class RequestData:
    """
        RequestData
    """
    BASE_URL = 'https://randomuser.me/api/'

    def __init__(self, count: str, *args, **kwargs):
        '''
        __init__ initiliaze dan gelir ve class olusturulurken kullanilan bir fonksiyondur.
        Icerisinde bulundugu class'a ait ozellik guncellenmistir.
        :param count:  parametre kullanimi ile base url den gelecek olan user belirlenebilmektedir.
        '''
        self.url = self.BASE_URL + '?result={}'.format(count)


    @error_handler #  Decorator kullanimi ile fonksiyondan donen sonucun status_code'u kontrol edilmis ve basarili ise
    # sonucun icerisindeki datanin result tipi dondurulmustur
    def _make_request(self):
        '''
        Make request ile istek calistirilir. BASER_URL'e gidilerek api a istek atilir. Gelen sonuc return edilir.
        Private fonksiyondur. Class disindan erisim istenmez, class icinden erisim uygundur. Istenilen durumlarda
        disaridan erisim yapilabilinir
        :return: request.models.Response tipinde sonuc doner.
        '''
        response = requests.get(self.url)
        return response


    @converter #  Decorator kullanimi ile yield'dan datanin goruntulebilinir ve kullanilabilir olmasi icin list tipine
    # cast etme islemi yapilmaktadir
    def get_location(self):
        '''
        User'in location bilgisini donen fonksiyondur.
        Class icerisindeki _make_request fonksiyonunu kullanarak gelen kullanicinin location bilgileri getirilebilinmektedir
        :return: List tipinde sonuc doner
        '''
        results = self._make_request()
        for item in results:
            yield item.get('location')

    @converter #  Decorator sayesinde sonuc list tipine cast edilmektedir.
    def get_login(self):
        '''
        User'in login bilgisini donen fonksiyondur.
        Class icerisindeki _make_request fonksiyonunu kullanarak gelen kullanicinin login bilgileri getirilebilinmektedir
        :return: List tipinde sonuc doner
        '''
        results = self._make_request()
        for item in results:
            yield item.get('login')

req = RequestData('11')
print(req.get_location())

# SORU 3 -------GET LOGIN--------------------
'''
    100 kere istek atilmis ve datalar username listesinin icerisine kaydedilmistir.
    100 istek biraz uzun surebilecegi icin sayiyi kuculterek deneyebilirsiniz
'''
username =[]
for i in range(100):
    temp = RequestData(i)
    username.append(temp.get_login()[0].get('username'))
print('------------LOGIN INFO-------------------')
print(username)

# SORU 4 -------GET LOCATION--------------------
'''
    api 20 istekte bulunulmus ve gelen datalarin street bilgileri location listinde tutularak ekrana yazdirilmistir.
'''
location = []
for i in range(20):
    temp = RequestData(i)
    location.append(temp.get_location()[0].get('street'))
print('-------------STREET INFO--------------')
print(location)










