import dashboard
import scanner
import subprocess

if __name__ == '__main__':
    devnull = subprocess.DEVNULL
    subprocess.Popen(['nohup', 'python3', 'scanner.py'], stdout=devnull, stderr=devnull)

    d = dashboard.Dashboard()
    d.start()
