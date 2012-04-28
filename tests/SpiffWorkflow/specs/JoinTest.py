import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from TaskSpecTest import TaskSpecTest
from SpiffWorkflow.specs import Join


class JoinTest(TaskSpecTest):
    CORRELATE = Join

    def create_instance(self):
        return Join(self.wf_spec,
                       'testtask',
                       description='foo')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(JoinTest)
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
