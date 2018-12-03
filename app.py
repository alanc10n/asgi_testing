import asyncpg
from envparse import env
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
import uvicorn

class Config:
    def parse(self):
        self.app_host = env('ASGI_HOST', default='0.0.0.0')
        self.app_port = env.int('ASGI_APP_PORT', default=8001)
        self.debug = env.bool('ASGI_DEBUG', default=True)

app = Starlette()
    
@app.route('/')
async def home(request):
    return PlainTextResponse("Howdy")

def main():
    config = Config()
    config.parse()
    app.debug = config.debug

    uvicorn.run(app, host=config.app_host, port=config.app_port)

if __name__ == '__main__':
    main()
