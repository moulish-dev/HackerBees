import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer


class IdeaGeneration(BaseHTTPRequestHandler):

    
    
    def do_GET(self):
        # Print debug message for start
        print("Request received")
        
        # Check if the requested path is root "/"
        if self.path == '/':
            file_path = 'hello.html'
            try:
                # Open and read the HTML file
                with open(file_path, 'r') as file:
                    html_content = file.read()
                
                # Send a 200 OK response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                # Write the HTML content to the response
                self.wfile.write(html_content.encode('utf-8'))
            
            # Handle file not found error
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            # Handle paths that are not "/"
            self.send_error(404, "Page not found")
    
    def do_POST(self):
        if self.path=='/name-submit':
            


    def create_team():
        if 
        team_names = []



def runserver(server_class=HTTPServer, handler_class=IdeaGeneration, port=8000):
    # Set up the server address and port
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    # Open the browser to localhost and specified port
    webbrowser.open(f'http://localhost:{port}/')
    
    print(f"Server starting on port {port}...")
    httpd.serve_forever()


# Run the server if this script is executed
if __name__ == '__main__':
    runserver()

