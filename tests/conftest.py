import os
import traceback
from datetime import datetime

import allure

from _pytest.config import hookimpl


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        if rep.when == 'call' and rep.failed:

            web_driver = item.module.driver
            screenshot_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]

            web_driver.save_screenshot("screenshots/%s.png" % screenshot_name)
            allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name='screenshot',
                    attachment_type=allure.attachment_type.PNG
            )
