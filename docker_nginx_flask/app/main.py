from pyfiglet import Figlet
import os
from flask import Flask

app = Flask(__name__)

font = Figlet(font="starwars")

@app.route('/')
def main():
    html_text = font.renderText("Docker")\
	    .replace(" ","&nbsp;")\
	    .replace(">","&gt;")\
	    .replace("<","&lt;")\
	    .replace("\n","<br>")

    # use a monospace font so everything lines up as expected
    return "<html><body style='font-family: monospace;'>" + html_text + "</body></html>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="80")
