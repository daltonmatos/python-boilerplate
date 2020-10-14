import os
from importlib import reload

from asynctest import TestCase, mock

from myproj import config


class ConfigTest(TestCase):
    async def test_debug_is_false(self):
        with mock.patch.dict(os.environ, DEV_DEBUG="0"):
            s = config.Settings()
            self.assertEqual(s.DEBUG, False)

    async def test_other_namespace(self):
        with mock.patch.dict(os.environ, NAMESPACE="PROD", PROD_DEBUG="0"):
            reload(config)
            s = config.Settings()
            self.assertEqual(s.DEBUG, False)
