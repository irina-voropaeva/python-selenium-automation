from pytest import fixture
from webdrivermanager import GeckoDriverManager


class BaseTest:

    @fixture(scope="session", autouse=True)
    def init(self):
        pass
