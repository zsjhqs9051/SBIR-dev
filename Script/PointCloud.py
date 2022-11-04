# -*- coding: utf-8 -*-
import open3d as op
import numpy as np
import copy as cp
import os
import matplotlib.pyplot as plt

# Point Cloud Transformation
def transform(source,transformation):
    """
    Param :source -> geometry
          :transformation -> [matrix 4 by 4]
    """
    source_temp = cp.deepcopy(source)
    source_temp.transform(transformation)
    return source_temp

# Creation of transforming matrix
def create_transformation_matrix(model,rotation,translation):
    """
        Param: model -> any geometry object in open3d
               rotation:tuple( 1 by 3: float)
               translation: [ 1 by 3: float]
    """
    # mesh = op.geometry.TriangleMesh.create_coordinate_frame()
    mesh_1 = cp.deepcopy(model).translate(translation)
    r = model.get_rotation_matrix_from_xyz(rotation)
    mesh_1.rotate(r,center=(0,0,0))

    trans = np.eye(4)
    trans[:3,:3] = r
    trans[0,3] = translation[0]
    trans[1,3] = translation[1]
    trans[2,3] = translation[2]

    return mesh_1,trans

def display_customization_render(*args,color = [0.5,0.7,0.4]):
    """
    Param: *args -> geometry list
            color -> [float:range(0,1),3 by 1]
    """
    vis = op.visualization.Visualizer()
    vis.create_window(window_name = '',
    width = 1920,height = 1080,left = 50,top = 50
    )

    for gm in args:
        vis.add_geometry(gm)
    render_option = vis.get_render_option()
    render_option.background_color = np.asarray(color)
    render_option.mesh_show_back_face = True
    render_option.mesh_show_wireframe = True
    render_option.show_coordinate_frame = False
    vis.run()
    vis.destroy_window()

# Downsampling of Point Cloud and Computation of FPFH Feature
def down_sample(pc,size = 0.01, radius_for_normals_estimate = 0.02, radius_for_feature = 0.04, max_nearest_n = 30 ):
    """
        voxel down sample of point cloud and Computation of FPFH
        Param:pc -> PointCloud
              size, radius_for_normals_estimate, radius_for_feature -> float
              return: pc_down -> PointClound
                      pc_fpfh -> feature on each point

    """
    params = [size,radius_for_normals_estimate,radius_for_feature]
    if np.all(params) == False:
        raise ValueError

    pc_down = pc.voxel_down_sample(size)
    pc_down.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = radius_for_normals_estimate,max_nn = max_nearest_n))
    pc_fpfh = op.pipelines.registration.compute_fpfh_feature(
        pc_down,
        op.geometry.KDTreeSearchParamHybrid(radius = radius_for_feature,max_nn = max_nearest_n)
    )
    return pc_down,pc_fpfh

# Fast Global Registration Optimization
def fast_global_registration(source,target,source_fpfh,target_fpfh,maximum_distance,iter_number = 30):
    """
        Param:source,target -> PointCloud
              source_fpfh, target_fpfh -> feature on each point
              maximum_distance -> float: maximum corresponding point distance between point clouds
              iter_number -> int: iteration number
              return: Registration_result -> Registraction_result.transformation matrix: [float:4 by 4]
    """

    Registration_result = op.pipelines.registration.registration_fast_based_on_feature_matching(
        source,target,source_fpfh,target_fpfh,
        op.pipelines.registration.FastGlobalRegistrationOption(maximum_correspondence_distance = maximum_distance,
                                                    iteration_number = iter_number
        )
    )

    return Registration_result

def fast_global_registration_with_track(source,target,source_fpfh,target_fpfh,maximum_distance,
                                        radius_normal,iter_number = 50, max_nearest_n = 30):

    """
        fast global registration with tracking the process of registration
        Param:source,target -> PointCloud
              source_fpfh, target_fpfh -> feature on each point
              maximum_distance -> float: maximum corresponding point distance between point clouds
              radius_normal -> float: estimate of point normal with radius_normal
              iter_number -> int: iteration number for tracking the process of registration,default = 50
    """
    vis = op.visualization.Visualizer()
    vis.create_window(window_name = '',
    width = 1920,height = 1080,left = 0,top = 0)
    vis.add_geometry(source)
    vis.add_geometry(target)
    vis.get_render_option().background_color = np.asarray([0.2,0.4,0.6])

    source.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = radius_normal,max_nn = max_nearest_n ))
    target.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = radius_normal,max_nn = max_nearest_n ))

    if not os.path.exists('./global_registration_process_tracking'):
        os.makedirs('./global_registration_process_tracking')

    for i in range(iter_number):
        result = op.pipelines.registration.registration_fast_based_on_feature_matching(
        source,target,source_fpfh,target_fpfh,
        op.pipelines.registration.FastGlobalRegistrationOption(maximum_correspondence_distance = maximum_distance,
                                                    iteration_number = 1 )
        )

        source.transform(result.transformation)
        vis.update_geometry(source)
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(f'./global_registration_process_tracking/GlobalRegistration{i+1:04d}.png')
    vis.run()
    vis.destroy_window()

# Using iterative closest point registration
def local_iterative_closest_point(source,target,kdtree_radius,registration_maximum_distance,transformation,max_nearest_n = 30):

    """
        Param:source,target -> PointCloud
              kdtree_radius -> float
              registration_maximum_distance -> float: maximum corresponding point distance between point clouds
              transformation -> initial transformation matrix: [float: 4 by 4]
              max_nearest_n -> int: the maximum number of the nearest points
              return: result -> result.transformation matrix: [float:4 by 4]
    """
    source.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = kdtree_radius, max_nn = max_nearest_n))
    target.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = kdtree_radius, max_nn = max_nearest_n))
    result = op.pipelines.registration.registration_icp(source,target,registration_maximum_distance,transformation,
                            op.pipelines.registration.TransformationEstimationPointToPlane()
    )
    return result

def local_iterative_closest_point_with_track(source,target,kdtree_radius,registration_maximum_distance,
                                            transformation,iter_number = 50, max_nearest_n = 30):
    """
        Param:source,target -> PointCloud
              kdtree_radius -> float
              registration_maximum_distance -> float: maximum corresponding point distance between point clouds
              transformation -> initial transformation matrix: [float: 4 by 4]
              iter_number -> int: iteratin number for the track process
              max_nearest_n -> int: the maximum number of the nearest points
              return: result -> result.transformation matrix: [float:4 by 4]
    """
    vis = op.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(source)
    vis.add_geometry(target)
    source.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = kdtree_radius,max_nn = max_nearest_n ))
    target.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = kdtree_radius,max_nn = max_nearest_n ))

    if not os.path.exists('./IcpTrack'):
        os.makedirs('./IcpTrack')

    for i in range(iter_number):
        result = op.pipelines.registration.registration_icp(source,target,registration_maximum_distance,transformation,
                                op.pipelines.registration.TransformationEstimationPointToPlane(),
                                op.pipelines.registration.ICPConvergenceCriteria(max_iteration = 1)
        )
        source.transform(result.transformation)
        vis.update_geometry(source)
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(f'./IcpTrack/Icp{i:04d}.png')
    vis.destroy_window()

def surface_reconstruction(target,kdtree_radius = 0.5,max_nearest_n = 30,octree_depth = 14):
    """
        Param: target -> PointCloud
               kdtree_radius -> float
               max_nearest_n -> int: the maximum number of the nearest points
               return mesh -> surface mesh instant
                      poisson_density -> list:float

    """
    print('executing the surface reconstruction')
    target.estimate_normals(op.geometry.KDTreeSearchParamHybrid(radius = kdtree_radius,max_nn = max_nearest_n))
    triangle_mesh, poisson_density = op.geometry.TriangleMesh.create_from_point_cloud_poisson(target, depth = octree_depth)
    triangle_mesh.paint_uniform_color([0,1,0])

    return triangle_mesh,poisson_density

# removal of the low vertices density after the surface reconstruction
def vertex_density(mesh,poisson_density,cmap = 'viridis',density_percentage_removal = 0.01):
    """
    Param: mesh -> TriangleMesh
           poisson_density: one of return value from surface reconstruction algorithm
           density_percentage_removal: float: range(0,1)
    """
    vd = np.asarray(poisson_density)
    density_color = plt.get_cmap(cmap)((vd-vd.min())/(vd.max()-vd.min()))
    density_color = density_color[:,:3]

    mesh.vertex_colors = op.utility.Vector3dVector(density_color)
    removal_of_vertices = vd < np.quantile(vd, density_percentage_removal)
    mesh.remove_vertices_by_mask(removal_of_vertices)

    return mesh

def connected_mesh_cluster_removal(mesh):
    """
    Param: mesh -> TriangleMesh

    """
    print("Connected triangles Processing and classification")
    connected_mesh_clusters_index, triangles_n_per_cluster, area_per_cluster = mesh.cluster_connected_triangles()

    connected_mesh_clusters_index = np.asarray(connected_mesh_clusters_index)
    triangles_n_per_cluster = np.asarray(triangles_n_per_cluster)
    area_per_cluster = np.asarray(area_per_cluster)
    print(connected_mesh_clusters_index)
    print(triangles_n_per_cluster)

    largest_cluster_idx = triangles_n_per_cluster.argmax()
    triangles_to_remove = connected_mesh_clusters_index != largest_cluster_idx
    mesh.remove_triangles_by_mask(triangles_to_remove)
    # color = plt.get_cmap(cmap)()
    # color = color[:,:3]
    # mesh.vertex_colors = op.utility.Vector3dVector(color)
    mesh.paint_uniform_color([1,0,0])
    mesh.compute_triangle_normals()

    return mesh

def dbscan_filter(pcd,eps = 0.3,min_points = 10,noise_color = [1.0,0.0,0.0]):
    """
        Param: pcd -> PointCloud
               eps -> radius for scanning data noise: float
               min_points: minimum of points with radius classified to the same cluster:int
               noise_color: [ 3 by 1: float: range(0,1)]
    """

    labels = np.asarray(pcd.cluster_dbscan(eps = eps,min_points = min_points))
    label_max = labels.max()
    print(f'This point cloud has {label_max+1} clusters')
    colors = plt.get_cmap('tab20')(labels/(label_max if label_max > 0 else 1))
    colors[labels<0] = noise_color
    ind = np.where(labels<0)[0]
    pcd_noise = pcd.select_by_index(ind)
    pcd_noise.colors = op.utility.Vector3dVector(colors[labels<0][:,:3])
    pcd_filtered = pcd.select_by_index(ind,invert = True)
    pcd_filtered.colors = op.utility.Vector3dVector(colors[labels>=0][:,:3])

    return pcd_filtered,pcd_noise
