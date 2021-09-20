def application(environ, start_response):
	status = '200 OK'
	output = b'Hello World! Testing my first python app using CI/CD pipeline'
	response_headers = [('Content-type', 'text/plain'),('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]

