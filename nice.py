from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

SNARKS = [
  'sassy pants', 'silly', 'suck it', 'not so wow', 'man-bun'
]


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        <p>Hi! This is the home page.</p>
        <a href = "/hello">Go to Hello</a>
        <a href="/diss">Go to Diss</a>
      </body>
    </html>
      


      """

def generate_compliments_html():
  """Generate string of compliments with html tags."""

  final_string = ""

  for compliment in AWESOMENESS:
    final_string += "<option value='%s'>%s</option>" % (compliment, compliment)

  return final_string

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          Choose term to boost your ego:
          <select name="compliment">
            %s
          <input type="submit">
        </form>
      </body>
    </html>
    """ % (generate_compliments_html())


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)




@app.route('/diss')
def choose_diss():
    """prompt for user's name and pick snarks."""

    return """
      <!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi There!</h1>
          <form action="/snark">
            <label>What's your name? <input type="text" name="person"></label>
            <br>
            Choose term to deflate your ego:
            <select name="snark">
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
              <option value="%s">%s</option>
            <input type="submit">
          </form>
        </body>
      </html>
      """ % (SNARKS[0], SNARKS[0], SNARKS[1], SNARKS[1], 
        SNARKS[2], SNARKS[2], SNARKS[3], SNARKS[3], SNARKS[4], SNARKS[4])

@app.route('/snark')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    snark = request.args.get("snark")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Snark</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, snark)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
