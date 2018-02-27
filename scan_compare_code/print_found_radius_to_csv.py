# -*- coding: utf-8 -*-
# port of
# http://pointclouds.org/documentation/tutorials/cylinder_segmentation.php
# you need to download
# http://svn.pointclouds.org/data/tutorials/table_scene_mug_stereo_textured.pcd

import pcl
import sys
import pprint

pts = sys.argv[1]
cloud = pcl.load(pts) 
#print "cloud size:"

#print(cloud.size)

fil = cloud.make_passthrough_filter()
fil.set_filter_field_name("z")
fil.set_filter_limits(0, .5)#set crop length along z axis
cloud_filtered = fil.filter()
#print "filetered size:"
#print(cloud_filtered.size)

seg = cloud_filtered.make_segmenter_normals(ksearch=50)
seg.set_optimize_coefficients(True)
seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
seg.set_normal_distance_weight(0.1)
seg.set_method_type(pcl.SAC_RANSAC)
seg.set_max_iterations(100)
seg.set_distance_threshold(0.03)
indices, model = seg.segment()

#print "filtered model:"
#pprint.pprint(model)

cloud_plane = cloud_filtered.extract(indices, negative=False)
# NG : const char* not str
# cloud_plane.to_file('table_scene_mug_stereo_textured_plane.pcd')
#pcl.save(cloud_plane,"water"+ str(pts))

cloud_cyl = cloud_filtered.extract(indices, negative=True)

seg = cloud_cyl.make_segmenter_normals(ksearch=50)
seg.set_optimize_coefficients(True)
seg.set_model_type(pcl.SACMODEL_CYLINDER)
seg.set_normal_distance_weight(0.1)
seg.set_method_type(pcl.SAC_RANSAC)
seg.set_max_iterations(10000)
seg.set_distance_threshold(0.05)
seg.set_radius_limits(0.5, 2)
indices, model = seg.segment()

#print"found cylinder model:"
#pprint.pprint(model]
print(str(pts) +", "+ str(model[-1]))

cloud_cylinder = cloud_cyl.extract(indices, negative=False)
# NG : const char* not str
# cloud_cylinder.to_file("table_scene_mug_stereo_textured_cylinder.pcd")
#pcl.save(cloud_cylinder,"cyl"+str(pts))
