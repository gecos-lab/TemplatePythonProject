import opengeode as og 
import opengeode_geosciences as ogg
import geode_numerics
import geode_implicit 
import geode_explicit
import geode_simplex

print("Hello Geode world!")

bbox_min = og.Point3D([0, 0, 0])
bbox_max = og.Point3D([10, 10, 10])
print("Two points have been created: ("+
      str(bbox_min.value(0))+"," +str(bbox_min.value(1))+","+str(bbox_min.value(2))+
      ") and ("+str(bbox_max.value(0))+"," +str(bbox_max.value(1))+","+str(bbox_max.value(2))+")"
      )

bbox = og.BoundingBox3D()
bbox.add_point(bbox_min)
bbox.add_point(bbox_max)
center = bbox.center()
print("The aligned bounding box defined is centered arround ("+str(center.value(0))+"," +str(center.value(1))+","+str(center.value(2))+")")
print("Ciao!")

