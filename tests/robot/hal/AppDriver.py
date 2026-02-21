import subprocess

class AppDriver:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def start(self):
        self.p = subprocess.Popen(
            ["embedded/hal/app_test.exe"],
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
