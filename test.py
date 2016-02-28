from moulinex import mesh
from moulinex import light
from moulinex import camera
from moulinex import render
from moulinex import general
from moulinex import modifier
from moulinex import colors


def main():
    general.setup(100)
    mesh.passive_underground()
    mesh.create_room()
    light.create_light(scale=(20, 20, 20), location=(0, 0, 20))

    ball = mesh.add_ball(color=colors.BLUE)
    modifiers = []
    for i in range(0, 3):
        ar_mod = modifier.Modifier(ball)
        ar_mod.add_modifier()
        ar_mod.set_amount(6)
        ar_mod.set_offset(i)
        ar_mod.apply_modifier()
        modifiers.append(ar_mod)

    modifiers[0].seperate_parts()
    modifiers[0].origin_to_geometry()

    camera.create_dof_camera()
    general.bake()
    # render.render_to_vid()
    render.render_to_still(frame=100)

main()
