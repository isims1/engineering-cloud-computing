import connexion
import six
import os, platform, subprocess, re

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server import util

def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command, shell=True).strip()
    elif platform.system() == "Linux":
        return "Linux YEAAAAA"
    return "cannot find cpuinfo"

def cpu_get():  # noqa: E501
    """cpu_get

    Returns cpu information of the hosting server # noqa: E501


    :rtype: CPU
    """
    return CPU(get_processor_name())
