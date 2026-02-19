import subprocess

class app_driver:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def start(self):
        self.p = subprocess.Popen(
            ["embedded/app_test.exe"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

    def send(self, cmd):
        self.p.stdin.write(cmd + "\n")
        self.p.stdin.flush()
        return self.p.stdout.readline().strip()

    def stop(self):
        self.p.terminate()
