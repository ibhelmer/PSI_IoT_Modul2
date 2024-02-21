from microdot import Microdot

app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello PSI and PSU :-)'

@app.route('/version')
async def version(request):
    return 'Version 0.5/UCN'

if __name__ == '__main__':
    app.run(port=80)