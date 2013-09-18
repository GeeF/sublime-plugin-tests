# TODO: Break out fixed content of `add_test` into test suite, allowing `add_test` to be dynamic
# TODO: I strongly dislike not having a loose single file BDD framework (e.g. mocha, jasmine)
from lib.framework import TestCase

# Load in 3rd party dependencies
from jinja2 import Template

class TestLeftDelete(TestCase):
    def parse_io_files(self, base_path):
        # Load in input
        with open('%s.input.py' % base_path) as f:
            input = f.read()

        # Break up target selection from content
        input_obj = self.split_sel(input)

        # Load in single.output
        with open('%s.output.py' % base_path) as f:
            expected_output = f.read()

        # Break up expected selection from content
        expected_obj = self.split_sel(expected_output)

        # Return collected information
        info = {
            'target_sel': input_obj['sel'],
            'content': input_obj['content'],
            'expected_sel': expected_obj['sel'],
            'expected_content': expected_obj['content'],
        }

        # TODO: Make this into a decorator (from TestCase)
        # Template and return plugin
        plugin = None
        with open('test_files/plugin.template.py') as f:
            template = Template(f.read())
            plugin = template.render(**info)
        return plugin

    def test_left_delete_single(self):
        return self.parse_io_files('example/left_delete/test_files/single')

    def test_left_delete_multi(self):
        return self.parse_io_files('example/left_delete/test_files/multi')

    def test_left_delete_multi_collapse(self):
        return self.parse_io_files('example/left_delete/test_files/multi_collapse')
