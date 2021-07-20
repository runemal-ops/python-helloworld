from flask import Flask, json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    ## log line
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    response_data = {
        "result": "OK - healthy",
    }
    response = app.response_class(
        response = json.dumps(response_data),
        status = 200,
        mimetype ='application/json'
    )
    ## log line
    app.logger.info('Status request successful')
    return response

@app.route("/metrics")
def metrics():
    response_data = {
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }
    response = app.response_class(
        response = json.dumps(response_data),
        status = 200,
        mimetype ='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )
    
    app.run(host='0.0.0.0')
