# render_ray.py
#    Ray tracing rendering algorithms

from ren3d.ray3d import Interval, Point, Ray
from ren3d.models import Record
from ren3d.rgb import RGB
from math import inf

EPSILON = 10e-12

def raytrace(scene, img, updatefn=None):
    """basic raytracing algorithm to render scene into img
    """
    camera = scene.camera
    w, h = img.size
    camera.set_resolution(w, h)
    for j in range(h):
        for i in range(w):
            ray = camera.ij_ray(i, j)
            color = raycolor(scene, ray, Interval(), scene.reflections)
            img[i, j] = color.quantize(255)
        if updatefn:
            updatefn()


def raycolor(scene, ray, interval, reflections):
    """returns the color of ray in the scene
    """
    hit = Record()
    if not scene.objects.intersect(ray, interval, hit):
        return scene.background

    # hitobj = hit.object
    # apply Blinn-Phong shading
    k = hit.color
    if scene.textures and hit.texture:
            uvn = hit.textcoords
            ambient = diffuse = hit.texture(uvn)
    else:
        ambient = k.ambient
        diffuse = k.diffuse

    # compute ambient color
    color = ambient * scene.ambient

    # Lambert component
    for light in scene.lights:
        lpos, lcolor = light
        lvec = (lpos-hit.point)
        shadray = Ray(hit.point, lvec)
        if (scene.shadows
            and scene.objects.intersect(shadray, Interval(EPSILON, 1), Record())):
            continue
        lvec.normalize()
        color += diffuse * max(0.0, lvec.dot(hit.normal)) * lcolor

        # specular component
        vvec = -ray.dir.normalized()
        hvec = vvec + lvec
        hvec.normalize()
        color += max(0.0, hvec.dot(hit.normal))**k.shininess * lcolor * k.specular

    if k.reflect and reflections > 0:
        refldir = ray.dir.reflection(hit.normal)
        reflray = Ray(hit.point, refldir)
        color += raycolor(scene, reflray, Interval(EPSILON, inf), reflections-1) * k.reflect
        
        
    return color
