# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

####################################
# IMPORT MODULES
####################################

from . import app_handler
from . import ot_batch_fake_user
from . import ui_batch_fake_user
from . import ui_user_prefs
# from . import pt_manage_datablocks

bl_info = {
    "name": "Automatic Fake-User",
    "author": "Carlos Mu <carlos.damian.munoz@gmail.com>",
    "blender": (2, 93, 0),
    "version": (1, 2, 0),
    "category": "Interface",
    "location": "Addon Preferences, File Menu",
    "description": "Automate fake-user assigment to avoid loss of orphan datablocks",
    "warning": "",
    "doc_url": "https://blendermarket.com/products/automatic-fake-user",
    "tracker_url": "https://blendermarket.com/creators/carlosmu",
}

####################################
# REGISTER/UNREGISTER
####################################
def register():
    app_handler.register()
    ot_batch_fake_user.register()
    ui_batch_fake_user.register()
    ui_user_prefs.register()
    # pt_manage_datablocks.register()

def unregister():
    app_handler.unregister()
    ot_batch_fake_user.unregister()
    ui_batch_fake_user.unregister()
    ui_user_prefs.unregister()
    # pt_manage_datablocks.unregister()