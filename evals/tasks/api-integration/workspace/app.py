from router import Router
from service import version,items

def build_app():
    app=Router()
    app.register('GET','/version',version)
    app.register('GET','/items',items)
    return app
