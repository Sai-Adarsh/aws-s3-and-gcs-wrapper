### Run
  ```bash
  # Build the Image
  $ docker build -t simple-flask-app:latest .

  # Run the Docker container using the command shown below
  $ docker run -d -p 5000:5000 simple-flask-app
  ```

The application will be accessible at ```http://localhost:5000```. If you are using boot2docker, find the IP address using $ boot2docker ip, and then use the IP at ```http://<host_ip>:5000```.

### Run Flask server without Docker.
  ```bash
  # Create a virtualenv and activate it
  $ virtualenv venv && source venv/bin/activate
  
  # Install Python dependencies.
  $ pip install -r requirements.txt

  # Run
  $ python app.py
  ```
The application can be accessed at ```http://localhost:5000```

### Deploy
You can deploy your own copy of the API using this button.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
