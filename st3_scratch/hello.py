import sublime
import sublime_plugin

# TODO: This wait loop should look for plugin_host running
def wait_a_sec():
    sublime.run_command('tmp_test_hey')
sublime.set_timeout(wait_a_sec, 1000)
print(sublime.version())

class TmpTestHeyCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        f = open('/tmp/hey3', 'w')
        f.write('hello')
        f.close()