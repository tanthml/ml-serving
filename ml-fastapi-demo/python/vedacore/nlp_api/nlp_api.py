from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


# config root route
ROOT_ROUTE = "/nlp-api/v1"


class NLPApi:
    def __init__(self, app_config=None):
        self.app_config = app_config
        self.middleware = [
            Middleware(
                CORSMiddleware,
                allow_origins=['*'],
                allow_credentials=True,
                allow_methods=['*'],
                allow_headers=['*']
            )
        ]
        self.app = FastAPI(middleware=self.middleware)

    def __call__(self, *args, **kwargs):
        return self._create_app()

    def _create_app(self):
        from vedacore.nlp_api.v1 import nlp_sentiment

        app = self.app

        @app.get(f"/")
        async def get_root():
            return RedirectResponse(url='/docs')

        # for nlp tasks
        app.include_router(
            nlp_sentiment.router,
            prefix=f"{ROOT_ROUTE}"
        )

        return app
