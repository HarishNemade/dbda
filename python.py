
import http.server
import socketserver

# Define the handler to use for incoming requests
handler = http.server.SimpleHTTPRequestHandler

# Set the port number for the server
port = 8080

# Create the server and bind it to the specified port
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port}")
print("Harish")

# Run the server indefinitely
httpd.serve_forever()
print ("harish")
a =10 
b = 20

