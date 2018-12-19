import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAACZBLl1Q82QBAGDM8UckaYp2cuuE69ylZApK3HDjm9Vp5ZBujW7HHtGndbaO15aClpf8AnZCg1XjXPNTOtCGPIct5STlKG2hMOWiuKMRqsFmY8JISG616vsyZCZCEsjZBVQAJDAAr4ujNKMf3jqm8wJZA4h2wmUAizsDLImoNYngdeKDMhIwIKi"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):

def send_button_message(id, text, buttons):
    pass
"""
