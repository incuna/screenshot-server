from flask import Flask, request
import envoy

LOCAL_PATH = '/Users/jcdt/Desktop/'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def screenshot():
    if 'path' in request.form:
        path = request.form['path']        
        r = envoy.run(str('screencapture -tjpg %s%s.jpg' % (LOCAL_PATH, path))) #, data='data to pipe in', timeout=2)
        
        if (r.status_code):
            return "Error %s: %s" % (r.status_code, r.std_err)
        else:
            return "Sucess %s: %s" % (r.status_code, r.std_out)
                    
    return ''

if __name__ == "__main__":
    app.run(debug=True)