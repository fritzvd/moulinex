import bpy
import mathutils


class Modifier(object):

    def __init__(self, blender_object):
        self.blender_object = blender_object
        self.name = ''
        self.modifier = None
        self.applied = False
        self.deselect_all()

    def deselect_all(self):
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in bpy.data.objects:
            obj.select = False

    def add_modifier(self, modifier='ARRAY',
                     extra_params={}):
        bobj = self.blender_object
        bpy.context.scene.objects.active = bobj
        bobj.select = True
        bpy.ops.object.modifier_add(type=modifier)
        self.modifier = bobj.modifiers[0]
        self.name = self.modifier.name
        return self

    def set_offset(self, direction):
        self.modifier.use_relative_offset = True
        self.modifier.relative_offset_displace = mathutils.Vector((0, 0, 0))
        self.modifier.relative_offset_displace[direction] = 1

    def apply_and_seperate(self):
        self.apply_modifier()
        self.seperate_parts()
        self.origin_to_geometry()
        return self.applied

    def set_amount(self, amount):
        self.modifier.count = amount

    def apply_modifier(self):
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=self.name)
        self.applied = True

    def seperate_parts(self):
        bpy.context.scene.objects.active = self.blender_object
        # seperate parts
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.separate(type='LOOSE')

    def origin_to_geometry(self):
        bpy.context.scene.objects.active = self.blender_object
        # back to object mode set gravity center
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
