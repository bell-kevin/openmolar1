#! /usr/bin/python

# ########################################################################### #
# #                                                                         # #
# # Copyright (c) 2009-2016 Neil Wallace <neil@openmolar.com>               # #
# #                                                                         # #
# # This file is part of OpenMolar.                                         # #
# #                                                                         # #
# # OpenMolar is free software: you can redistribute it and/or modify       # #
# # it under the terms of the GNU General Public License as published by    # #
# # the Free Software Foundation, either version 3 of the License, or       # #
# # (at your option) any later version.                                     # #
# #                                                                         # #
# # OpenMolar is distributed in the hope that it will be useful,            # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of          # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           # #
# # GNU General Public License for more details.                            # #
# #                                                                         # #
# # You should have received a copy of the GNU General Public License       # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.      # #
# #                                                                         # #
# ########################################################################### #

'''
This module provides a function 'run' which will move data
to schema 3.7
'''


import logging

from openmolar.schema_upgrades.database_updater_thread \
    import DatabaseUpdaterThread

LOGGER = logging.getLogger("openmolar")

SQLSTRINGS = [
    '''
CREATE TABLE IF NOT EXISTS locations (
serialno INT(11) NOT NULL,
location CHAR(1),
PRIMARY KEY (serialno),
FOREIGN KEY (serialno) REFERENCES new_patients(serialno)
)
    ''',
]

CLEANUPSTRINGS = []


class DatabaseUpdater(DatabaseUpdaterThread):

    '''
    a class to update the database
    '''

    def run(self):
        LOGGER.info("running script to convert from schema 3.6 to 3.7")
        try:
            self.connect()
            # - execute the SQL commands
            self.progressSig(10, _("creating new tables"))
            self.execute_statements(SQLSTRINGS)
            self.progressSig(97, _('updating settings'))
            LOGGER.info("updating stored database version in settings table")

            self.update_schema_version(("3.7",), "3.6 to 3.7 script")

            self.progressSig(100, _("updating stored schema version"))
            self.commit()
            self.completeSig(_("Successfully moved db to") + " 3.7")
            return True
        except Exception as exc:
            LOGGER.exception("error upgrading schema")
            self.rollback()
            raise self.UpdateError(exc)


if __name__ == "__main__":
    dbu = DatabaseUpdater()
    if dbu.run():
        LOGGER.info("ALL DONE, conversion successful")
    else:
        LOGGER.warning("conversion failed")
