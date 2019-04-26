import os
import subprocess


class PathReader:
    @staticmethod
    def read_path():
        return os.path.expanduser(
            subprocess.check_output(
                'read -e -p "You> " var; echo $var',
                shell=True
            ).strip().decode("utf-8")
        )
