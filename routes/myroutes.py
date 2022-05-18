from config import app

@app.get('/message')
def greetnow():
    return "This is home page...Hi How arey you?"

@app.get('/number')
def fun():
    return "12345"