# render_ray.py
#    Ray tracing rendering algorithms
# by: John Zelle

from ren3d.ray3d import Interval, Point, Ray
from ren3d.models import Record
from ren3d.rgb import RGB


def raytrace(scene, img, updatefn=None):
    """basic raytracing algorithm to render scene into img
    """
    camera = scene.camera
    w, h = img.size
    camera.set_resolution(w, h)
    for j in range(h):
        for i in range(w):
            ray = camera.ij_ray(i, j)
            color = raycolor(scene, ray, Interval())
            img[i, j] = color.quantize(255)
        if updatefn:
            updatefn()


def raycolor(scene, ray, interval):
    """returns the color of ray in the scene
    """

    info = Record()
    if scene.objects.intersect(ray, interval, info):
        K = info.color
        hitpoint = info.point
        n = info.normal
        color = K.ambient * scene.ambient
        for lpos, lcolor in scene.lights:
            lvec = (lpos - hitpoint).normalized()
            shadray = Ray(hitpoint, lpos-hitpoint)
            if scene.shadows and scene.objects.intersect(shadray, Interval(0.0001, 1), Record()):
                continue
            lambert = max(0, lvec.dot(n))
            color += K.diffuse * lambert

            vvec = -ray.dir.normalized()
            h = (lvec + vvec).normalized()
            color += K.specular * lcolor * (max(0, h.dot(n)) ** K.shininess)
        return color
    return scene.background


