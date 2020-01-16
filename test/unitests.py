import unittest
import parsing.file_parsing as pars
from objects import module as mod
from objects import project as pro


class Tests(unittest.TestCase):
    def test_get_imports(self):
        self.assertEqual(pars.get_imports("sample_code.py"),
                         ['parsing.file_parsing', 'objects.file', 'objects.function', 'os', 're'])

    def test_get_function_def(self):
        self.assertEqual(pars.get_function_def("sample_code.py"),
                         ['make_list_all_source_files', 'prepare_data_to_visualisation',
                          'prepare_functions_data_to_visualisation'])

    def test_get_function_calls(self):
        self.assertEqual(pars.get_function_calls("sample_code.py").sort(),
                         ['walk', 'search', 'append', 'make_list_all_source_files', 'pars', 'any', 'append', 'append',
                          'File', 'append', 'make_list_all_source_files', 'get_list_of_defined_functions',
                          'pars_for_functions', 'any', 'append', 'append', 'Function', 'append', 'get_size'].sort())

    def test_pars_for_files(self):
        self.assertEqual(mod.pars_for_files(".").sort(), ['__init__.py', 'sample_code.py', 'unitests.py'].sort())

    def test_pars_for_modules(self):
        self.assertEqual(pro.pars_for_modules("."), ['global_scope'])


if __name__ == '__main__':
    unittest.main()
