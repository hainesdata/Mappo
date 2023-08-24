import dashboard
import scanner
import subprocess

if __name__ == '__main__':
    subprocess.Popen(['python3', 'scanner.py'])
    subprocess.Popen(['python3', 'dashboard.py'])

    s = scanner.Scanner()
    s.run()

    d = dashboard.Dashboard()
    d.start()

# if __name__ == '__main__':
#     scanner_script_path = 'scanner.py'
#     subprocess.Popen(['python3', scanner_script_path])
#
#     # TODO: Create separate debug window for scanner.py
#     # venv_path = '~/python-venv'
#     # scanner_script_path = '~/PycharmProjects/Mappo/scanner.py'
#     # subprocess.Popen(f"osascript -e 'tell app \"Terminal\" to do script \"source {venv_path}/bin/activate && python3 {scanner_script_path}\"'", shell=True)
#
#     # TODO: Figure out why output is duplicated
#     print('Starting Dash app...')
#     d = dashboard.Dashboard()
#     d.start()