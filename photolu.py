from io import BytesIO
import requests


def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)
    response = upload.photo_messages(f)[0]
    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']
    return owner_id, photo_id, access_key


def send_photo(owner_id, photo_id, access_key):
    attachment =[]
    attachment.append(f'photo{owner_id}_{photo_id}_{access_key}')
    return attachment
