import requests


def send_request(url, method="GET", payload={}, headers={}):
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def count_words(response):
    splited_response = list(response.replace(" ", ""))
    word_count = len(splited_response)
    return f"Character count: {word_count}"


def main():
    response = send_request(url="http://SimpleWebServerALB-388820569.us-east-1.elb.amazonaws.com")
    return count_words(response=response)


if __name__ == "__main__":
    print(main())