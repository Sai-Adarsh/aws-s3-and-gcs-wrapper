from flask import Flask, jsonify, request
import os
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from werkzeug import secure_filename
from configparser import ConfigParser

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def default():
    return jsonify({'result': 'config success'})

@app.route("/put_data", methods = ['GET', 'POST'])
def putData():
    if request.method == 'POST':
        file = request.files['file']
        bucket_name = request.form['bucket_name']
        if file and bucket_name:
            filename = secure_filename(file.filename)
            file.save(os.path.join('static', filename))
            put_path = os.path.join('static', 'put_data.sh')
            my_env = os.environ.copy()
            my_env["FILE_NAME_ENV"] = filename
            my_env["BUCKET_NAME"] = str(bucket_name)
            session = Popen([put_path], stdout=PIPE, stderr=PIPE, env = my_env)
            stdout, stderr = session.communicate()
            print(stdout.decode('utf-8'))
            return jsonify({'result': 'put success'})
        return jsonify({'result': 'no file received'})
    return jsonify({'result': 'no file received'})

@app.route("/put_dir", methods = ['GET', 'POST'])
def putDir():
    if request.method == 'POST':
        file = request.form['file']
        bucket_name = request.form['bucket_name']
        if file and bucket_name:
            put_path = os.path.join('static', 'put_dir.sh')
            my_env = os.environ.copy()
            my_env["FILE_NAME_ENV"] = file
            my_env["BUCKET_NAME"] = str(bucket_name)
            session = Popen([put_path], stdout=PIPE, stderr=PIPE, env = my_env)
            stdout, stderr = session.communicate()
            print(stdout.decode('utf-8'))
            return jsonify({'result': 'put dir success'})
        return jsonify({'result': 'no folder received'})
    return jsonify({'result': 'no folder received'})


@app.route("/get_data", methods = ['GET', 'POST'])
def getData():
    if request.method == 'POST':
        file = request.files['file']
        bucket_name = request.form['bucket_name']
        if file and bucket_name:
            filename = secure_filename(file.filename)
            file.save(os.path.join('static', filename))
            put_path = os.path.join('static', 'get_data.sh')
            my_env = os.environ.copy()
            my_env["FILE_NAME_ENV"] = filename
            my_env["BUCKET_NAME"] = 's3://' + bucket_name + '/' + filename
            session = Popen([put_path], stdout=PIPE, stderr=PIPE, env = my_env)
            stdout, stderr = session.communicate()
            print(stdout.decode('utf-8'))
            return jsonify({'result': 'get success'})
        return jsonify({'result': 'no file received'})
    return jsonify({'result': 'no file received'})

@app.route("/switch_config", methods = ['GET', 'POST'])
def switchConfig():
    if request.method == 'POST':
        base = request.form['base']
        my_env = os.environ.copy()
        conf_file = my_env["HOME"]+"/.s3cfg"
        config = ConfigParser()
        config.read(conf_file)
        if base == "AWS":
            config.set("DEFAULT", "access_key", "AKIAYJRWIDIGPWY2IP6Y")
            config.set("DEFAULT", "secret_key", "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")
            config.set("DEFAULT", "host_base", "s3.amazonaws.com")
            config.set("DEFAULT", "host_bucket", "%(bucket)s.s3.amazonaws.com")
            config.set("DEFAULT", "gpg_passphrase", "-==o#^D-W^@}|SY")
        elif base == "GCP":
            config.set("DEFAULT", "access_key", "GOOG25VC3TC4WUVONNTR54BG")
            config.set("DEFAULT", "secret_key", "V64GvVZv49rxlLynWQkhtj4aeb+lAPMyhoP+lkb6")
            config.set("DEFAULT", "host_base", "storage.googleapis.com")
            config.set("DEFAULT", "host_bucket", "%(bucket).storage.googleapis.com")
            config.set("DEFAULT", "gpg_passphrase", "")
        else:
            return jsonify({'result': 'switched_config'})
        with open(conf_file, 'w') as f:
            config.write(f)
        return jsonify({'result': 'switched_config'})

@app.route("/get_dir", methods = ['GET', 'POST'])
def getDir():
    if request.method == 'POST':
        bucket_name = request.form['bucket_name']
        if bucket_name:
            put_path = os.path.join('static', 'get_dir.sh')
            my_env = os.environ.copy()
            my_env["BUCKET_NAME"] = 's3://' + bucket_name
            session = Popen([put_path], stdout=PIPE, stderr=PIPE, env = my_env)
            stdout, stderr = session.communicate()
            print(stdout.decode('utf-8'))
            return jsonify({'result': 'get directory success'})
        return jsonify({'result': 'no directory received'})
    return jsonify({'result': 'no directory received'})

@app.route("/list_buckets", methods = ['GET', 'POST'])
def listBuckets():
    if request.method == 'POST':
        put_path = os.path.join('static', 'list_buckets.sh')
        session = Popen([put_path], stdout=PIPE, stderr=PIPE)
        stdout, stderr = session.communicate()
        return jsonify({'result': stdout.decode('utf-8')})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
