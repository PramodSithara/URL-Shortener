import requests


def shorten_link(full_link, link_name):
    API_KEY = ''                            #cutt.ly api key
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print(data)

    try:
        title = data['url']['title']
        shorten_link = data['url']['shortLink']

        print('Title: ', title)
        print('Link: ', shorten_link)
    
    except:
        status = data['url']['status']
        print('Error Status:',status)

link = input('Enter a Link: >> ')
name = input('Give Your link a name: >> ')

shorten_link(link, name)


