import webbrowser

f = open('helloworld.html', 'w')

message = """<html>
<title>Hello</title>
<head></head>
<body><h1>Welcome to IT101-2P</h1>
<p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')