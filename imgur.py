import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient

client_id = '66ee31ff9e2f383'
client_secret = '8b0e9dcb239c23e76f273dcaaea58db1cdf84368'
album_id = 'EuCqN0p'
access_token = 'a16244300de0c76dceb364a2e148859b1bdf69e9'
refresh_token = 'f222e54114427cbba1b1243d589196bc5ca66c94'

def showImgur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {
        'album': album_id,
        'name': fileName,
        'title': fileName,
        'description': str(datetime.date.today())
    }

    try:
        print('[log:INFO]Uploading image...')
        imgurl = client.upload_from_path(fileName + '.png', config=config, anon=False)['link']
        print('[log:INFO]Done upload...')
    except:
        imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
        print('[log:ERROR]Unable upload...')

    return imgurl