#!C:\Python38\python.exe

print("Content-Type: text/html; charset=UTF-8\n")

print("<html>")
print("<head>")
print("<title>drop down filter</title>")

print("<meta charset=\"utf-8\">")
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css\">")
print("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script>")
print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js\"></script>")
print("<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js\"></script>")
print("<style>")

print("#hzInput {")
print("padding: 20px;")
print("margin-top: -6px;")
print("border: 0;")
print("border-radius: 0;")
print(" color:white;")
print("background: black;")
print("}")

print("</style>")
print("</head>")

print("<body>")

print("<div class=\"container\">")
print("<div class=\"dropdown\">")

print("<button class=\"btn btn-primary dropdown-toggle\" type=\"button\" data-toggle=\"dropdown\">")
print("filter</button>")
print("<ul class=\"dropdown-menu\">")
print("<input class=\"form-control\" id=\"hzInput\" type=\"text\" placeholder=\"Search..\">")
print("<li><a href=\"#\">HTML</a></li>")
print("<li><a href=\"#\">CSS</a></li>")
print("<li><a href=\"#\">JS</a></li>")
print("<li><a href=\"#\">jQuery</a></li>")
print("<li><a href=\"#\">SQL</a></li>")
print("<li><a href=\"#\">PHP</a></li>")
print("</ul>")
print("</div>")
print("</div>")
print("</body>")


print("<script>")
print("$(document).ready(function(){")
print("$(\"#hzInput\").on(\"keyup\", function() {")
print("var value = $(this).val().toLowerCase();")
print("$(\".dropdown-menu li\").filter(function() {")
print("$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)")
print("});")
print("});")
print("});")

print("</script>")

print("</html>")
