import html_to_json
import requests

url = "http://example.com:80"
url_html = requests.get(url)

json_ = html_to_json.convert(url_html.content)

print(json_)