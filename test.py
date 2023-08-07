try:
    # import app
    from app import app
    import unittest

except Exception as e:
    print("ERROR. Missing dependencies {}".format(e))


class FlaskTest(unittest.TestCase):
    # Comprovar que la resposta de la ruta / és 200
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code
        self.assertEqual(status, 200)

    # Comprovar que la ruta home retorna el missatge "Hello World"
    def test_home_message(self):
        tester = app.test_client(self)
        response = tester.get("/")
        message = response.data
        self.assertEqual(message, b"Hello World")

    # Comprovar la resposta de la ruta /currency_rates
    def test_currency_rates(self):
        tester = app.test_client(self)
        response = tester.get("/currency_rates")
        message = response.data
        print(response)
        status = response.status_code
        self.assertIn(b'{"from":"EUR","rate":"1.359","to":"USD"}', message)
        self.assertIn(b'{"from":"CAD","rate":"0.732","to":"EUR"}', message)
        self.assertIn(b'{"from":"USD","rate":"0.736","to":"EUR"}', message)
        self.assertIn(b'{"from":"EUR","rate":"1.366","to":"CAD"}', message)
        self.assertIn(b'{"from":"CAD","rate":"0.995","to":"USD"}', message)
        self.assertEqual(status, 200)

    # Comprovar la resposta de la ruta /currency_rate
    def test_currency_rate(self):
        tester = app.test_client(self)
        response = tester.get("/currency_rate?from=EUR&to=USD")
        message = response.data
        status = response.status_code
        self.assertIn(b"1.359", message)
        self.assertEqual(status, 200)


# Run the tests
if __name__ == "__main__":
    unittest.main()
