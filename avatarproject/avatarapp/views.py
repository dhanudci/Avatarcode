from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    if request.method == "POST":
        if 'avatar' in request.POST:
            input = request.POST.get('avatar','')
            url = "https://api.d-id.com/talks"

            pageload = {
                "script":{
                    "type":"text",
                    "input": input,
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
                "authorization": "Basic ZGhhbnVwcml5YS5hcml2YW5hbnRoYW1AZGNpLmlu:O4eE0eZRrWJZvQTv9FFz4"
            }


            response = requests.post(url, json=pageload, headers=headers)

            print(response.text)
            
            if request.method == "GET":
                url = "https://api.d-id.com/talks/id"
                # resulturl = request.GET.get('resulturl','')
                # result_url= resulturl
            #     pageload = {
            #         "result_url": result_url,
            # }
            
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": "Basic ZGhhbnVwcml5YS5hcml2YW5hbnRoYW1AZGNpLmlu:O4eE0eZRrWJZvQTv9FFz4"
            }


            response = requests.get(url,headers=headers)

            # print(response.text)


            return render(request,'success.html')
        # else:
        #     return render(request,'avatar.html')
    return render(request,'avatar.html')

# def avatar(request):
#     url= "https://api.d-id.com/talks/{id}"
#     if 'result_url' 

