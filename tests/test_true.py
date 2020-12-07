# Third party imports
from asynctest import TestCase
from {{cookiecutter.project_name}} import sum


class TestExample(TestCase):
    async def test_true(self):
        self.assertEqual(2, sum(1, 1))
