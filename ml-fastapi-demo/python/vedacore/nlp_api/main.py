import logging
import os

import click
import uvicorn

from nlp_api import NLPApi
from config import ProdConfig, Config


@click.command()
@click.option('--default_env', type=click.Choice(['DEV', 'PROD'], case_sensitive=False))
@click.option('--port', type=int, default=8080)
@click.option('--host', type=str, default='0.0.0.0')
def main(default_env, port, host):
    os.environ['DEFAULT_ENV'] = default_env if default_env else 'DEV'
    app_config = ProdConfig if default_env == 'PROD' else Config
    app = NLPApi(app_config=app_config)()

    logging.info('****************** Starting Server *****************')
    uvicorn.run(app, host=host, port=int(port), debug=app_config.DEBUG)


if __name__ == '__main__':
    main()
