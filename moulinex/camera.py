import bpy


def create_dof_camera(dof_object=None):
    # Add a camera fish eye.
    # cam_loc = mathutils.Vector((15, -5, 5))

    bpy.ops.object.camera_add(
        view_align=True,
        location=(22, -17, 15),
        rotation=(0, 0, 0))
    camera = bpy.context.active_object
    # Euler((1.1093189716339111, 0.010816991329193115,
    # 0.8149281740188599), 'XYZ')
    camera.rotation_euler[0] = 1.1
    camera.rotation_euler[1] = 0
    camera.rotation_euler[2] = 0.8
    camera.data.type = 'PERSP'
    camera.data.sensor_width = 22.20
    camera.data.sensor_height = 14.7

    if dof_object:
        bpy.data.cameras[0].dof_object = dof_object

    # Activate camera
    bpy.context.scene.camera = camera


def create_fish_eye():
    # Add a camera fish eye.
    # cam_loc = mathutils.Vector((15, -5, 5))
    bpy.ops.object.camera_add(
        view_align=True,
        location=(15, -5, 5),
        rotation=(0, 0, 0)
        )
    camera = bpy.context.active_object
    # Euler((1.1093189716339111,
    # 0.010816991329193115, 0.8149281740188599), 'XYZ')
    camera.rotation_euler[0] = 1.1
    camera.rotation_euler[1] = 0
    camera.rotation_euler[2] = 0.8
    camera.data.type = 'PANO'
    camera.data.cycles.fisheye_lens = 2.7
    camera.data.cycles.fisheye_fov = 3.14159
    camera.data.sensor_width = 8.8
    camera.data.sensor_height = 6.6

    # Activate camera
    bpy.context.scene.camera = camera
