import webbrowser

f = open('CPC2\Exercise #5.html', 'w')

message = """<html>
<title>My First HTML</title>
<head></head>
<body><h1>Welcome to My First HTML Program Using Python!</h1>
<h2>My name is John Sebastian Ablay</h2>
<p>Thank you!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('CPC2\Exercise #5.html')
