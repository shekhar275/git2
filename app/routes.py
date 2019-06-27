from app import app

@app.route('/')
@app.route('/index')
def index():
    return"""
    <html>
    <head><title> GOOD DAY </title>
    </head>
    hello world good day
    </html>"""
    
