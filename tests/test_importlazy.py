"""
To run this test:
1. cd importlazy/tests
2. python -m unittest test_importlazy.py
"""

import unittest
import sys


class ImportLazyTest(unittest.TestCase):

    def test1_initial_state(self):
        """Initially, the module must not exist in the imported modules.
        The package or module should not be imported during the initial state.
        """
        assert 'test_importlazy' in sys.modules
        assert 'test_project' not in sys.modules
        assert 'test_project.path' not in sys.modules
        assert 'a_module' not in sys.modules

    def test2_importing_module_only_when_used(self):
        """The package must exist in the imported modules.
        Followed by the module once the attribute of it is used.
        """
        import test_project
        # The package will be imported but not the modules
        assert 'test_project' in sys.modules
        assert 'test_project.path' in sys.modules
        assert 'test_project.a_module' not in sys.modules

        # As the class attribute of the module is used,
        # the module will be imported for the first time
        assert str(type(test_project.path.ClassOne)) == "<class 'type'>"
        assert 'test_project.a_module' in sys.modules

        # Check that we can really create an instance of the imported class
        one = test_project.path.ClassOne()
        from test_project.a_module import AModuleClassOne
        assert isinstance(one, AModuleClassOne)

