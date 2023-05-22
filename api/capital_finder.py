from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
class handler(BaseHTTPRequestHandler):

    
    """
    A simple HTTP request handler that retrieves information about countries and their capitals.

    Usage:
      Send a GET request to the server with the following query parameters:
        - 'country': Specify the name of a country to get its capital.
            You should search by country in the following address: "https://capital-finder-pannwog2t-theteaser.vercel.app/api/capital_finder?country=<Country Name Here>"
        - 'capital': Specify the name of a capital to get the corresponding country.
            You should search by capital in the following address: "https://capital-finder-pannwog2t-theteaser.vercel.app/api/capital_finder?capital=<Capital Name Here>"
    
    """

    def do_GET(self):

        path = self.path
        url_components = parse.urlsplit(path)
        query_Parts = parse.parse_qsl(url_components.query)
        dict_of_queries = dict(query_Parts)
        country_name = dict_of_queries.get("country")
        capital_name = dict_of_queries.get("capital")
        if country_name:
            url = f"https://restcountries.com/v3.1/name/{country_name}"
            res = requests.get(url)
            data = res.json()
            result = data[0]["capital"][0]
            location = f"The capital of {country_name} is {result}."
        elif capital_name:
            url = f"https://restcountries.com/v3.1/capital/{capital_name}"
            res = requests.get(url)
            data = res.json()
            result = data[0]["name"]["official"]
            location = f"{capital_name} is the capital of {result}."
        else:
            location = "Please insert a valid inquiry!"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(location.encode('utf-8'))
        return
    


# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import platform
# # import requests
# class handler(BaseHTTPRequestHandler):


#     def do_GET(self):

#         path = self.path
#         print(path)
#         url_components=parse.urlsplit(path)
#         print(url_components)
#         query_strings_list = parse.parse_qsl(url_components.query)
#         print(query_strings_list)
#         dic = dict(query_strings_list)
#         print(dic)
#         name= dic.get("name")
#         print(name)

#         if name:
#             message= f"Aloha {name}"
#         else:
#             message= f"Aloha Stranger"

#         message += f"\n Greetings from python version {platform.python_version()}"
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(message.encode('utf-8'))
#         return