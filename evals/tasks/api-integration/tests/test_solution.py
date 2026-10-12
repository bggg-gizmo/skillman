import unittest
from app import build_app
from service import health
from router import Router
class Tests(unittest.TestCase):
    def test_health_service(self):
        self.assertEqual(health(),{'status':'ok','service':'skillman-demo'})
    def test_health_route(self):
        self.assertEqual(build_app().dispatch('GET','/health'),(200,{'status':'ok','service':'skillman-demo'}))
    def test_existing_routes(self):
        app=build_app()
        self.assertEqual(app.dispatch('GET','/version'),(200,{'version':'1.0.0'}))
        self.assertEqual(app.dispatch('GET','/items'),(200,{'items':['alpha','beta']}))
    def test_unknown_and_method(self):
        self.assertEqual(build_app().dispatch('GET','/missing'),(404,{'error':'not found'}))
        self.assertEqual(build_app().dispatch('POST','/health'),(404,{'error':'not found'}))
    def test_router_duplicate_protection(self):
        router=Router();router.register('GET','/x',lambda:{})
        with self.assertRaises(ValueError):router.register('GET','/x',lambda:{})
