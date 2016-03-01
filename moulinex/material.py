"""
A number of materials that can be used with the cycles renderer. These are all
node-based shaders.

* add_mix_material - adds a mix shader, as default a plastic like glossy shader
* add_material - adds a material with a name or as default: DiffuseBSFD

"""

import bpy


def add_mix_material(
    bobj,
    name,
    shader1='ShaderNodeBsdfDiffuse',
    shader2='ShaderNodeBsdfGlossy',
    color=(0.8, 0.2, 0.216, 0.9)
):
    """Add material that mixes different shaders.
    The most common mix shader I use, is the one that most resembles opaque
    plastic. It uses a Glossy and a Diffuse shader with Fresnel as a fraction
    input.

    Keyword arguments:
    bobj -- blender object you want to apply the material to.
    name -- name of the material.
    shader1 -- first input for the mix shader - Defaults to DiffuseBSFD
    shader2 -- second input for the mix shader - Defaults to GlossyBSFD
    color -- 4 dimensional vector RGBA style (red, green, blue, alpha)
    """
    FRESNEL = 'ShaderNodeFresnel'
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True

    # Remove default
    material.node_tree.nodes.remove(
        material.node_tree.nodes.get('Diffuse BSDF'))
    material_output = material.node_tree.nodes.get('Material Output')
    new_shader_material = material.node_tree.nodes.new('ShaderNodeMixShader')
    shader1_mat = material.node_tree.nodes.new(shader1)
    shader1_mat.inputs['Color'].default_value = color
    shader2_mat = material.node_tree.nodes.new(shader2)
    shader2_mat.inputs[1].default_value = 0
    fresnel = material.node_tree.nodes.new(FRESNEL)

    material.node_tree.links.new(
        new_shader_material.inputs[0], fresnel.outputs[0])
    material.node_tree.links.new(
        new_shader_material.inputs[1], shader1_mat.outputs[0])
    material.node_tree.links.new(
        new_shader_material.inputs[2], shader2_mat.outputs[0])

    bobj.active_material = material
    material.node_tree.links.new(
        material_output.inputs[0], new_shader_material.outputs[0])
    return new_shader_material


def add_material(bobj, name,
                 shader='ShaderNodeBsdfDiffuse', color=(0.8, 0.8, 0.8, 0.9)):
    """Adds a 'simple' shader to the blender object you pass it.

    Keyword arguments:
    bobj -- blender object you want to apply the material to.
    name -- name of the material.
    shader -- Defaults to DiffuseBSFD
    color -- 4 dimensional vector RGBA style (red, green, blue, alpha)
    """
    # Create a new material
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True

    if shader != 'ShaderNodeBsdfDiffuse':
        # Remove default
        material.node_tree.nodes.remove(
            material.node_tree.nodes.get('Diffuse BSDF'))
        material_output = material.node_tree.nodes.get('Material Output')
        new_shader_material = material.node_tree.nodes.new(shader)
        bobj.active_material = material
        material.node_tree.links.new(
            material_output.inputs[0], new_shader_material.outputs[0])
    else:
        new_shader_material = material.node_tree.nodes.get('Diffuse BSDF')

    new_shader_material.inputs['Color'].default_value = color
    return material, new_shader_material
