#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2015, Francesco "dfirfpi" Picasso <francesco.picasso@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Windows DPAPI BLOB info report."""

import optparse
import os
import sys

try:
    from DPAPI.Core import blob
    from DPAPI.Core import masterkey
    from DPAPI.Core import registry
except ImportError:
    raise ImportError('Missing dpapick, install it or set PYTHONPATH.')


def check_parameters(options, args):
    """Simple checks on the parameters set by the user."""
    if not args or not len(args) == 1:
        sys.exit('You must provide an argument.')
    elif not os.path.isfile(args[0]):
        sys.exit('Argument must be a file.')

if __name__ == '__main__':
    """Utility core."""
    usage = (
        'usage: %prog [*no-options*] BLOB file.\n\n'
        'It tries to parse the input file and it reports the BLOB properties.')

    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    check_parameters(options, args)

    try:
        blob = blob.DPAPIBlob(open(args[0], 'rb').read())
        print blob
    except:
        print '\nBLOB parsing failure! See next details.\n'
        raise
