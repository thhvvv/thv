#!/usr/bin/python3
from app import create_app

# Create the app with the 'development' configuration
app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
