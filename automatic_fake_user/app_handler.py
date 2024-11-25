import bpy # type: ignore
from bpy.app.handlers import persistent # type: ignore

@persistent
def assign_on_save(scene):
    D = bpy.data
    C = bpy.context
    prefs = C.preferences.addons[__package__].preferences

    if prefs.assign_on_save:
        set_fake_users(D, prefs)

def set_fake_users(D, prefs):
    if prefs.actions:
        for act in D.actions:
            if not prefs.excluded in act.name:
                act.use_fake_user = True
            else:
                pass
    if prefs.materials:
        for mat in D.materials:
            if not prefs.excluded in mat.name:
                mat.use_fake_user = True
            else:
                pass
    if prefs.images:
        for img in D.images:
            if not prefs.excluded in img.name:
                img.use_fake_user = True
            else:
                pass
    if prefs.geometry_nodes:
        for ngr in D.node_groups:
            if ngr.type == 'GEOMETRY':
                if not prefs.excluded in ngr.name:
                    ngr.use_fake_user = True
                else:
                    pass
    if prefs.shader_groups:
        for ngr in D.node_groups:
            if ngr.type == 'SHADER':
                if not prefs.excluded in ngr.name:
                    ngr.use_fake_user = True
                else:
                    pass
    if prefs.worlds:
        for wor in D.worlds:
            if not prefs.excluded in wor.name:
                wor.use_fake_user = True
            else:
                pass
                

def register():
    bpy.app.handlers.save_pre.append(assign_on_save)

def unregister():
    bpy.app.handlers.save_pre.remove(assign_on_save)