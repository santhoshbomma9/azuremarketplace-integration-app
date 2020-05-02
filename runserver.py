"""
This script runs the azuremarketplace_integration_app application using a development server.
"""

from os import environ
from amp_app.webapp import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
