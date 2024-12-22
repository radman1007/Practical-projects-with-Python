from jinja2 import Environment, FileSystemLoader
import jdatetime

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")
output = template.render(name="index")
with open(r"templates/new-template.html", mode="w", encoding='utf-8') as tm:
    tm.write(output)
    