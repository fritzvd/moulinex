import bpy
import mathutils

from moulinex.material import add_mix_material, add_material


def add_ball(location=(0, 15, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(
        location=location,
        )
    bpy.ops.object.shade_smooth()
    bpy.ops.rigidbody.object_add()
    add_mix_material(bpy.context.active_object, 'Glossy Mix')
    return bpy.context.active_object


def passive_underground():
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))
    bpy.ops.rigidbody.objects_add()
    mesh = bpy.context.active_object
    mesh.name = 'Underground'
    mesh.scale = mathutils.Vector((20, 20, 20))
    bpy.ops.rigidbody.object_add()
    mesh.rigid_body.type = 'PASSIVE'
    material, new_shader_material = add_material(mesh, 'DiffuseUnderground')
    mesh.active_material = material
    return mesh


def add_modifier(bobj, direction, amount, size, modifier='ARRAY', height=0):
    for obj in bpy.data.objects:
        obj.select = False

    bpy.context.scene.objects.active = bobj
    bobj.select = True
    bpy.ops.object.modifier_add(type=modifier)

    modifier = bobj.modifiers[0]
    modifier.use_relative_offset = True
    modifier.relative_offset_displace = mathutils.Vector((0, 0, 0))
    modifier.relative_offset_displace[direction] = size + 1

    if direction == 1:
        new_direction = modifier.relative_offset_displace[direction] * - 1
        modifier.relative_offset_displace[direction] = new_direction
    modifier.count = amount
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modifier.name)

    bpy.context.scene.objects.active = bobj
    # seperate parts
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.separate(type='LOOSE')

    # back to object mode set gravity center
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


def duplicate_object(scene, name, copyobj):

    # Create new mesh
    mesh = bpy.data.meshes.new(name)

    # Create new object associated with the mesh
    ob_new = bpy.data.objects.new(name, mesh)

    # Copy data block from the old object into the new object
    ob_new.data = copyobj.data.copy()
    ob_new.scale = copyobj.scale
    ob_new.location = copyobj.location

    # Link new object to the given scene and select it
    scene.objects.link(ob_new)
    ob_new.select = True

    return ob_new
