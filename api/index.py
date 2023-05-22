from http.server import BaseHTTPRequestHandler

 
class handler(BaseHTTPRequestHandler):
  
  '''
  This is the serverless function that returns Hello world. 
  Link: https://capital-finder-xi-neon.vercel.app/api
  '''

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write("Hello world".encode())
    return