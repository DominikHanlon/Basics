r = request.get('https://www.google.com/', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()
