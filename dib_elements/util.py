# Copyright 2013, Red Hat Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import logging
import subprocess
import sys

def call(*args, **kwargs):

    logging.debug('executing command: %s' % args)
    p = subprocess.Popen(*args, stdout=sys.stdout,
                         stderr=sys.stderr, **kwargs)
    rc = p.wait()
    logging.debug('  exited with code: %s' % rc)
    return
