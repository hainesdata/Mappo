import dashboard
import subprocess


if __name__ == '__main__':
    scanner_script_path = 'scanner.py'
    devnull = subprocess.DEVNULL
    subprocess.Popen(['nohup', 'python3', scanner_script_path], stdout=devnull, stderr=devnull)

    print('Starting Dash app...')
    d = dashboard.Dashboard()
    d.start()
