from .utsg_decorators import (name, description,
                              max_points, points_lost_on_failure,
                              include_in_results, hidden,
                              message, output, images)
from .utsg_test_result import UTSGTestResult
from .utsg_testcase import UTSGTestCaseInfo, UTSGTestCase, UngradableError
from .utsg_types import AccessControls, PrairieLearnImage, PrairieLearnTestCaseJsonDict, UTSGTestStatus
from .run_tests import run_tests
# if we dynamically the decorators and we needed to import them, the below code would do it
# from . import utsg_decorators
# module_name_space = globals()
# for member in dataclasses.fields(UTSGTestCaseInfo):
#     try:
#         module_name_space[member.name] = getattr(utsg_decorators, member.name)
#     except AttributeError:
#         pass
# del module_name_space['utsg_decorators']
