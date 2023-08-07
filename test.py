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


# Run the tests
if __name__ == "__main__":
    unittest.main()
