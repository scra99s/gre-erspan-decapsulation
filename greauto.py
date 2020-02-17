#!/usr/bin/env python3

import subprocess
result = subprocess.run(['ip -br addr|cut -d" " -f1'], stdout=subprocess.PIPE)

interfaceList = result.stdout.decode('utf-8').splitlines())
