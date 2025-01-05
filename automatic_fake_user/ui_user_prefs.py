import bpy # type: ignore

##############################################
#    USER PREFERENCES 
##############################################

class AFU_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    ##################
    # Data Types 
    meshes : bpy.props.BoolProperty(
        name = "Meshes",
        description = "Set Fake Users in all meshes",
        default = False
    ) # type: ignore
    actions : bpy.props.BoolProperty(
        name = "Actions",
        description = "Set Fake Users in all actions",
        default = True
    ) # type: ignore
    materials : bpy.props.BoolProperty(
        name = "Materials",
        description = "Set Fake Users in all materials",
        default = False
    ) # type: ignore
    images : bpy.props.BoolProperty(
        name = "Images",
        description = "Set Fake Users in all images",
        default = False
    ) # type: ignore
    geometry_nodes : bpy.props.BoolProperty(
        name = "Geometry Nodes",
        description = "Set Fake Users in all geometry nodes",
        default = True
    ) # type: ignore
    shader_groups : bpy.props.BoolProperty(
        name = "Shader Groups",
        description = "Set Fake Users in all shader groups",
        default = True
    ) # type: ignore
    worlds : bpy.props.BoolProperty(
        name = "Worlds",
        description = "Set Fake Users in all worlds",
        default = False
    ) # type: ignore

    ###################
    # Preferences
    excluded : bpy.props.StringProperty(
        name = "If name contains",
        description = "ignore all datablock that that include this word",
        default = "exclude"
    ) # type: ignore
    assign_on_save : bpy.props.BoolProperty(
        name = "Assign on save",
        description = "Set fake-users to all enabled data-types when file is saving (Ctrl+S)",
        default = True
    ) # type: ignore
    enable_manual_button : bpy.props.BoolProperty(
        name = "Enable manual button",
        description = "By pressing the menu: file -> batch fake user",
        default = True
    ) # type: ignore
    
    ###################
    # UI          
    def draw(self, context):
        layout = self.layout 
        layout.use_property_split = True
        layout.use_property_decorate = True
        
        box = layout.box()
        box.label(text="Assign fake-users for:", icon='PRESET')
        box.prop(self, "meshes")
        box.prop(self, "actions")
        box.prop(self, "materials")
        box.prop(self, "images")
        box.prop(self, "geometry_nodes")
        box.prop(self, "shader_groups")
        box.prop(self, "worlds")
        box.separator()

        box.label(text="Excluded datablocks:", icon='CANCEL')
        box.prop(self, "excluded")
        box.separator()

        box.label(text="Behaviour:", icon='ARMATURE_DATA')
        box.prop(self, "assign_on_save")
        box.prop(self, "enable_manual_button")
        box.separator()

        layout.separator()

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(AFU_Preferences) 
        
def unregister():
    bpy.utils.unregister_class(AFU_Preferences)