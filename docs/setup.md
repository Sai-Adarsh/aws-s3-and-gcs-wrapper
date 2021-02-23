### ☀️ Run

* Build the Image:
  ```bash
  $ docker build -t simple-flask-app:latest .
  ```
* Run the Docker container using the command shown below.
  ```bash
  $ docker run -d -p 5000:5000 simple-flask-app
  ```
* The application will be accessible at `http://127.0.0.1:5000` and if you are using `boot2docker`, find the IP address using `$ boot2docker ip` and the use the IP `http://<host_ip>:5000`


### ☀️ Run Flask Server without Docker

* Create a virtualenv and activate:
  ```bash
  $ virtualenv venv && source venv/bin/activate
  ```
* Install python dependencies
  ```bash
  $ pip install -r requirements.txt
  ```
* Install python dependencies
  ```bash
  $ python app.py
  ```
* The application will be accessible at `http://127.0.0.1:5000`
