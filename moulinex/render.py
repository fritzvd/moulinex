import bpy
import os


def render_to_still(file_name='out.png', file_path='./'):
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = os.path.join(file_path, file_name)
    bpy.ops.render.render(
        animation=False,
        write_still=True)


def render_to_vid(file_name='out.mp4', file_path='./', blur=False):
    bpy.context.scene.render.use_motion_blur = blur
    bpy.context.scene.render.image_settings.file_format = 'H264'
    bpy.context.scene.render.filepath =os.path.join(file_path, file_name)
    bpy.ops.render.render(animation=True)
