from bottle import route, run, static_file, request
from bottle import jinj2_template as template

@route('<path:path>')
def server_static(path):
    return static_file(path, root='/root/frankyao/telescope/html/')



if __name__ == '__main__':
	run(host='10.19.111.64',port=8080,reloader=True)
