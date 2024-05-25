import bpy # type: ignore
from . import app_handler 

class AFU_OT_batch_fake_user(bpy.types.Operator):
    """Assign fake-users to all enabled data types in addon preferences"""
    bl_idname = "afu.batch_fake_user"
    bl_label = "Batch Fake User"
    bl_options = {'REGISTER', 'UNDO'}

    ##############################################
    #   Apply Clipping functionality
    ##############################################
    def execute(self, context):
        D = bpy.data
        C = bpy.context
        prefs = C.preferences.addons[__package__].preferences
        if prefs.enable_manual_button:
            app_handler.set_fake_users(D, prefs)

            return{'FINISHED'}


##############################################
# REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(AFU_OT_batch_fake_user)

def unregister():
    bpy.utils.unregister_class(AFU_OT_batch_fake_user)