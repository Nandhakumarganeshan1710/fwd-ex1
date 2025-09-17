from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML page with colorful background and a table comparing TCP & IP
content = """
<!DOCTYPE html>
<html>
<head>
<title>TCP and IP Protocols</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: linear-gradient(to bottom right, #a8edea, #fed6e3); /* colorful gradient background */
    margin: 0;
    padding: 0;
  }
  h1 {
    text-align: center;
    color: #333;
    padding-top: 20px;
  }
  table {
    width: 70%;
    margin: 40px auto;
    border-collapse: collapse;
    background-color: #ffffff; /* white table background */
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-radius: 8px;
    overflow: hidden;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 12px 16px;
    text-align: left;
  }
  th {
    background-color: #4CAF50; /* green header */
    color: white;
    font-size: 18px;
  }
  tr:nth-child(even) {
    background-color: #f2f2f2; /* light grey for alternate rows */
  }
  tr:hover {
    background-color: #ddd; /* hover effect */
  }
</style>
</head>
<body>
  <h1>TCP and IP Protocols</h1>
  <table>
    <tr>
      <th>Feature</th>
      <th>IP (Internet Protocol)</th>
      <th>TCP (Transmission Control Protocol)</th>
    </tr>
    <tr>
      <td>Role</td>
      <td>Responsible for addressing and routing data between devices.</td>
      <td>Provides reliable, ordered delivery of data between applications.</td>
    </tr>
    <tr>
      <td>Connection</td>
      <td>Connectionless</td>
      <td>Connection-oriented</td>
    </tr>
    <tr>
      <td>Reliability</td>
      <td>No guarantee</td>
      <td>Guaranteed delivery with error checking and acknowledgements</td>
    </tr>
    <tr>
      <td>Layer</td>
      <td>Network Layer</td>
      <td>Transport Layer</td>
    </tr>
    <tr>
      <td>Use Cases</td>
      <td>Foundational for all internet communications (IP addresses)</td>
      <td>Web, email, file transfers (HTTP/HTTPS, FTP, SMTP)</td>
    </tr>
  </table>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

# Use a non-privileged port (8080) unless you run as admin/root
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("My TCP/IP website is running at http://localhost:8080 ...")
httpd.serve_forever()
