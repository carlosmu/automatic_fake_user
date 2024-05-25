import bpy # type: ignore

##############################################
## DRAW UI BUTTON
##############################################
def draw_batch_fake_user(self, context):
    prefs = context.preferences.addons[__package__].preferences
    layout = self.layout   
    if prefs.enable_manual_button:
        layout.separator()   
        layout.operator("afu.batch_fake_user", icon='FAKE_USER_ON')
    else:
        pass

##############################################
## Register/unregister classes and functions
##############################################
def register():
    bpy.types.TOPBAR_MT_file.append(draw_batch_fake_user)
        
def unregister():
    bpy.types.TOPBAR_MT_file.remove(draw_batch_fake_user)