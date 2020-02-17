#!/usr/bin/env python3

import subprocess
result = subprocess.run(['ip', 'link'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))


