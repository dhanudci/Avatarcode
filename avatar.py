import requests

url = "https://api.d-id.com/talks"

pageload = {
    "script":{
        "type":"text",
        "input":"Introduction In the world today millions of people are suffering from severe and complex diseases that are terminal or chronic in nature. The aftermath of these diseases is normally pain, distress, suffering, early death and grief to the people affected.Introduction The significance of nature and its purposive relationship with humans have been prevalent throughout the history of mankind. Its aspects affect human life in one way or another. For nature means more than just material abundance of the money-worshiping civilization.Introduction Contemporary business activities have become increasingly complex for entrepreneurs. This situation has compelled organizations to implement robust operational practices in an attempt to address the needs of employees, customers, suppliers, and competitors among other stakeholders.Information technology projects consist of many elements that contribute to their success or failure. This article focuses on planning and uncertainty dimensions like project size, diversity, and technical complexity. ",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural",
            "voice_config": {"style": "Cheerful"}
        }
    },
    "source_url":"https://i.ibb.co/qjr2Q1P/test7.jpg",
     "webhook": "https://host.domain.tld/to/webhook"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic MTltY2EwNUBhbWVyaWNhbmNvbGxlZ2UuZWR1Lmlu:SS6zvX_lRfy9R2lYkxxW1"
}


response = requests.post(url, json=pageload, headers=headers)

print(response.text)