#
# pylorax
# Install image and tree support data generation tool -- Python module.
#
# Copyright (C) 2008  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s): David Cantrell <dcantrell@redhat.com>
#

version = (0, 1)

__all__ = ['discinfo', 'treeinfo']

import discinfo
import treeinfo

def show_version(prog):
    """show_version(prog)

    Display program name (prog) and version number.  If prog is an empty
    string or None, use the value 'pylorax'.

    """

    if prog is None or prog == '':
        prog = 'pylorax'

    print "%s version %d.%d" % (prog, version[0], version[1],)
