from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers.image_search import router as image_search_router
from exceptions import register_error_handlers
import settings


app = FastAPI(title='Image Search Service',
              version='0.1.0',
              debug=settings.ENVIRONMENT == 'dev'
              )

app.add_middleware(CORSMiddleware,
                   allow_origins=settings.CORS_ORIGINS,
                   allow_methods=['GET', 'HEAD', 'OPTIONS',
                                  'POST', 'DELETE', 'PATCH'],
                   allow_credentials=True,
                   allow_headers=['*']
                   )


@app.get("/", tags=["root"])
async def get_root():
    return JSONResponse(status_code=200, content="Service operational")

app.include_router(image_search_router)

register_error_handlers(app)
