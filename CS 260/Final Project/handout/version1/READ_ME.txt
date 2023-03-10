Index of Files
--------------

Top-level

    Launchers:
    
	run_wf.py       -- create a wireframe image of a scene
      	run_rt.py       -- create an image via raytracing (simple progress)
      	run_art.py      -- create an image via raytracing with preview and display

    Simple Scene Examples:
    
        scene0.py  -- trivial single sphere scene
        scene1.py  -- a bunch of spheres
	scene2.py  -- just a box
	scene3.py  -- "table" with cube and spheres

In ren3d package

   Basic Building Blocks:

      math3d.py   -- Vectors and Points
      ray3d.py    -- Rays and Intervals
      rgb.py      -- RGB object for dealing with color values (ranges 0 to 1)
      
   Modeling and Rendering:

      camera.py     -- Object for setting up views in a scene      
      scenedef.py   -- Scene class and global scene and camera variables
      models.py     -- Code for objects that can be placed in scenes
      render_oo.py  -- Object-order rendering code
      render_ray.py -- Raytracing code

   Additional Files Required (copy to ren3d folder):

       image.py    -- Your PPM image class      
       ppmview.py  -- My class for showing images interactively
       matrix.py   -- Your matrix manipulation module

----------------------------------------------------------------------
Note: To run doc tests, invoke python in the top-level directory and execute
the module you want to run the tests in. For example:

$ python3 -m ren3d.math3d

