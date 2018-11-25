from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
import uvicorn

class Config:
    def __init__(self):
        self.app_host =  '0.0.0.0'
        self.app_port = 8001
        self.debug = True

config = Config()
    
app = Starlette(debug=config.debug)

@app.route('/')
async def home(request):
    return PlainTextResponse("Howdy")

if __name__ == '__main__':
    uvicorn.run(app, host=config.app_host, port=config.app_port)
