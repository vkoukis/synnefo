# Copyright (C) 2010-2014 GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from archipelagomapper import ArchipelagoMapper


class Mapper(object):
    """Mapper.
       Required constructor parameters: mappath, namelen.
       Optional mappool.
    """

    def __init__(self, **params):
        self.archip_map = ArchipelagoMapper(**params)

    def map_retr(self, maphash, blkoff=0, nr=100000000000000):
        """Return as a list, part of the hashes map of an object
           at the given block offset.
           By default, return the whole hashes map.
        """
        return self.archip_map.map_retr(maphash, blkoff, nr)

    def map_retr_archipelago(self, maphash, size):
        """Return as a list the hashes map of an Archipelago
        Volume.
        """
        return self.archip_map.map_retr_archipelago(maphash, size)

    def map_stor(self, maphash, hashes=(), blkoff=0, create=1):
        """Store hashes in the given hashes map."""
        self.archip_map.map_stor(maphash, hashes, blkoff, create)
