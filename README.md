# moulinex

Some blender utils I frequent.

## Installing

It doesn't look like blender supports dist-packages. The only packages it supports
are in-built, or add-on style plugins.

This isn't really a plugin, so I decided that for now this will make due:

```bash
  git clone https://github.com/fritzvd/moulinex.git
  cd moulinex
  echo "running Blender with test script"
  blender -P test.py
```

## Naming

![moulinex](doc/img/moulinex.jpg)

Whenever I think of a blender I picture this old-skool Moulinex blender.

## What does the test script do?
![test_out](doc/img/test_out.png)
It gives you a basic setup:
* walls
* mesh light
* adds a bunch of balls stacked in the scene
* adds physics
* bakes the physics
* renders the image shown above

If you uncomment to render the video, it renders this [video!](http://gfycat.com/UnderstatedBlissfulHairstreakbutterfly).
(Takes a while to have it render all the frames though)


# Usage
Starting a project with moulinex can be done as follows. Start a script in the root folder of the git project. And yes that sucks, but for now bear with me.
e.g. call it playing_with_moulinex.py

```python
from moulinex import general
from moulinex import mesh
from moulinex import camera

general.setup() # removes all default objects and sets renderer to 'cycles'
mesh.passive_underground() # creates a passive underground for a physics world
camera.create_dof_camera()
```

```bash
blender -P playing_with_moulinex.py
```

This will open up blender with the scene you just created. A blank slate with a passive underground and a camera.


## License
I made this, but I really don't care how you use it. For benefit, fun, profit.
As long as you're not using this to harass people or some heinous evil, it's all
good. So I guess an ISC license?

## Contributing
I love hearing about how you use this, or how you think this should be done
differently. Send me a pull request or catch me on [twitter: @fritzvd](https://twitter.com/fritzvd)
