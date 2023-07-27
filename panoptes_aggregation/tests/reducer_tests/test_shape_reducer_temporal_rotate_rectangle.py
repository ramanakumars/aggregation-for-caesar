from panoptes_aggregation.reducers.shape_reducer_dbscan import process_data as process_data_dbscan, shape_reducer_dbscan
from panoptes_aggregation.reducers.shape_reducer_hdbscan import process_data as process_data_hdbscan, shape_reducer_hdbscan
from panoptes_aggregation.reducers.shape_reducer_optics import process_data as process_data_optics, shape_reducer_optics
from .base_test_class import ReducerTest


extracted_data = [
    {
        "frame0": {
            "T0_toolIndex0_angle": [10.0],
            "T0_toolIndex0_displayTime": [0.1],
            "T0_toolIndex0_height": [50.0],
            "T0_toolIndex0_width": [150.0],
            "T0_toolIndex0_x_center": [510.0],
            "T0_toolIndex0_y_center": [500.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [12.0],
            "T0_toolIndex0_displayTime": [0.1],
            "T0_toolIndex0_height": [60.0],
            "T0_toolIndex0_width": [160.0],
            "T0_toolIndex0_x_center": [490.0],
            "T0_toolIndex0_y_center": [515.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [15.0],
            "T0_toolIndex0_displayTime": [0.1],
            "T0_toolIndex0_height": [60.0],
            "T0_toolIndex0_width": [120.0],
            "T0_toolIndex0_x_center": [510.0],
            "T0_toolIndex0_y_center": [500.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [30.0],
            "T0_toolIndex0_displayTime": [0.7],
            "T0_toolIndex0_height": [120.0],
            "T0_toolIndex0_width": [110.0],
            "T0_toolIndex0_x_center": [360.0],
            "T0_toolIndex0_y_center": [570.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [10.0],
            "T0_toolIndex0_displayTime": [0.9],
            "T0_toolIndex0_height": [50.0],
            "T0_toolIndex0_width": [140.0],
            "T0_toolIndex0_x_center": [520.0],
            "T0_toolIndex0_y_center": [510.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [10.0],
            "T0_toolIndex0_displayTime": [1.0],
            "T0_toolIndex0_height": [50.0],
            "T0_toolIndex0_width": [120.0],
            "T0_toolIndex0_x_center": [520.0],
            "T0_toolIndex0_y_center": [510.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [12.0],
            "T0_toolIndex0_displayTime": [0.9],
            "T0_toolIndex0_height": [50.0],
            "T0_toolIndex0_width": [150.0],
            "T0_toolIndex0_x_center": [530.0],
            "T0_toolIndex0_y_center": [500.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [25.0],
            "T0_toolIndex0_displayTime": [0.6],
            "T0_toolIndex0_height": [80.0],
            "T0_toolIndex0_width": [100.0],
            "T0_toolIndex0_x_center": [350.0],
            "T0_toolIndex0_y_center": [620.0],
        }
    },
    {
        "frame0": {
            "T0_toolIndex0_angle": [20.0],
            "T0_toolIndex0_displayTime": [0.9],
            "T0_toolIndex0_height": [140.0],
            "T0_toolIndex0_width": [80.0],
            "T0_toolIndex0_x_center": [350.0],
            "T0_toolIndex0_y_center": [580.0],
        }
    },
]

kwargs_extra_data = {
    'user_id': [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ]
}

processed_data = {
    'frame0': {
        'T0_toolIndex0': [
            (510.0, 500.0, 150.0, 50.0, 10.0, 0.1),
            (490.0, 515.0, 160.0, 60.0, 12.0, 0.1),
            (510.0, 500.0, 120.0, 60.0, 15.0, 0.1),
            (360.0, 570.0, 110.0, 120.0, 30.0, 0.7),
            (520.0, 510.0, 140.0, 50.0, 10.0, 0.9),
            (520.0, 510.0, 120.0, 50.0, 10.0, 1.0),
            (530.0, 500.0, 150.0, 50.0, 12.0, 0.9),
            (350.0, 620.0, 100.0, 80.0, 25.0, 0.6),
            (350.0, 580.0, 80.0, 140.0, 20.0, 0.9)
        ]
    },
    'shape': 'temporalRotateRectangle',
    'symmetric': False
}

reduced_data_dbscan = {
    "frame0": {
        "T0_toolIndex0_cluster_labels": [0, 0, 0, 1, 1, 1, 1, 1, 1],
        "T0_toolIndex0_clusters_count": [3, 6],
        "T0_toolIndex0_clusters_angle": [9.4, 21.5],
        "T0_toolIndex0_clusters_displayTime": [0.1, 0.9],
        "T0_toolIndex0_clusters_height": [60.7, 104.5],
        "T0_toolIndex0_clusters_sigma": [0.2, 0.5],
        "T0_toolIndex0_clusters_width": [138.0, 102.8],
        "T0_toolIndex0_clusters_x_center": [502.2, 352.3],
        "T0_toolIndex0_clusters_y_center": [503.9, 604.9],
        "T0_toolIndex0_temporalRotateRectangle_angle": [10.0, 12.0, 15.0, 30.0, 10.0, 10.0, 12.0, 25.0, 20.0],
        "T0_toolIndex0_temporalRotateRectangle_displayTime": [0.1, 0.1, 0.1, 0.7, 0.9, 1.0, 0.9, 0.6, 0.9],
        "T0_toolIndex0_temporalRotateRectangle_height": [50.0, 60.0, 60.0, 120.0, 50.0, 50.0, 50.0, 80.0, 140.0],
        "T0_toolIndex0_temporalRotateRectangle_width": [150.0, 160.0, 120.0, 110.0, 140.0, 120.0, 150.0, 100.0, 80.0],
        "T0_toolIndex0_temporalRotateRectangle_x_center": [510.0, 490.0, 510.0, 360.0, 520.0, 520.0, 530.0, 350.0, 350.0],
        "T0_toolIndex0_temporalRotateRectangle_y_center": [500.0, 515.0, 500.0, 570.0, 510.0, 510.0, 500.0, 620.0, 580.0]
    }
}

TestShapeReducerTemporalRotateRectangleDbscan = ReducerTest(
    shape_reducer_dbscan,
    process_data_dbscan,
    extracted_data,
    processed_data,
    reduced_data_dbscan,
    'Test shape temporalRotateRectangle reducer with DBSCAN',
    network_kwargs=kwargs_extra_data,
    pkwargs={'shape': 'temporalRotateRectangle'},
    kwargs={
        'eps': 0.5,
        'min_samples': 2,
        'metric_type': 'IoU',
    },
    test_name='TestShapeReducerTemporalRotateRectangleDbscan',
    round=1
)

reduced_data_optics = {
    "frame0": {
        "T0_toolIndex0_cluster_labels": [0, 0, 0, 2, 1, 1, 1, 2, 2],
        "T0_toolIndex0_clusters_angle": [9.4, 9.4, 20.0],
        "T0_toolIndex0_clusters_count": [3, 3, 3],
        "T0_toolIndex0_clusters_displayTime": [0.1, 0.9, 0.7],
        "T0_toolIndex0_clusters_height": [60.7, 51.4, 143.7],
        "T0_toolIndex0_clusters_sigma": [0.2, 0.2, 0.3],
        "T0_toolIndex0_clusters_width": [138.0, 137.4, 92.1],
        "T0_toolIndex0_clusters_x_center": [502.2, 522.5, 355.0],
        "T0_toolIndex0_clusters_y_center": [503.9, 509.1, 583.8],
        "T0_toolIndex0_temporalRotateRectangle_angle": [10.0, 12.0, 15.0, 30.0, 10.0, 10.0, 12.0, 25.0, 20.0],
        "T0_toolIndex0_temporalRotateRectangle_displayTime": [0.1, 0.1, 0.1, 0.7, 0.9, 1.0, 0.9, 0.6, 0.9],
        "T0_toolIndex0_temporalRotateRectangle_height": [50.0, 60.0, 60.0, 120.0, 50.0, 50.0, 50.0, 80.0, 140.0],
        "T0_toolIndex0_temporalRotateRectangle_width": [150.0, 160.0, 120.0, 110.0, 140.0, 120.0, 150.0, 100.0, 80.0],
        "T0_toolIndex0_temporalRotateRectangle_x_center": [510.0, 490.0, 510.0, 360.0, 520.0, 520.0, 530.0, 350.0, 350.0],
        "T0_toolIndex0_temporalRotateRectangle_y_center": [500.0, 515.0, 500.0, 570.0, 510.0, 510.0, 500.0, 620.0, 580.0]
    }
}


TestShapeReducerTemporalRotateRectangleOptics = ReducerTest(
    shape_reducer_optics,
    process_data_optics,
    extracted_data,
    processed_data,
    reduced_data_optics,
    'Test shape temporalRotateRectangle reducer with OPTICS',
    network_kwargs=kwargs_extra_data,
    pkwargs={'shape': 'temporalRotateRectangle'},
    kwargs={
        'min_samples': 2,
        'metric_type': 'IoU',
    },
    test_name='TestShapeReducerTemporalRotateRectangleOptics',
    round=1
)

reduced_data_hdbscan = {
    "frame0": {
        "T0_toolIndex0_cluster_labels": [0, 0, 0, 2, 1, 1, 1, 2, 2],
        "T0_toolIndex0_clusters_count": [3, 3, 3],
        "T0_toolIndex0_cluster_probabilities": [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.6, 0.7, 1.0],
        "T0_toolIndex0_clusters_angle": [9.4, 9.4, 20.0],
        "T0_toolIndex0_clusters_displayTime": [0.1, 0.9, 0.7],
        "T0_toolIndex0_clusters_height": [60.7, 51.4, 143.7],
        "T0_toolIndex0_clusters_persistance": [0.5, 0.6, 0.1],
        "T0_toolIndex0_clusters_sigma": [0.2, 0.2, 0.3],
        "T0_toolIndex0_clusters_width": [138.0, 137.4, 92.1],
        "T0_toolIndex0_clusters_x_center": [502.2, 522.5, 355.0],
        "T0_toolIndex0_clusters_y_center": [503.9, 509.1, 583.8],
        "T0_toolIndex0_temporalRotateRectangle_angle": [10.0, 12.0, 15.0, 30.0, 10.0, 10.0, 12.0, 25.0, 20.0],
        "T0_toolIndex0_temporalRotateRectangle_displayTime": [0.1, 0.1, 0.1, 0.7, 0.9, 1.0, 0.9, 0.6, 0.9],
        "T0_toolIndex0_temporalRotateRectangle_height": [50.0, 60.0, 60.0, 120.0, 50.0, 50.0, 50.0, 80.0, 140.0],
        "T0_toolIndex0_temporalRotateRectangle_width": [150.0, 160.0, 120.0, 110.0, 140.0, 120.0, 150.0, 100.0, 80.0],
        "T0_toolIndex0_temporalRotateRectangle_x_center": [510.0, 490.0, 510.0, 360.0, 520.0, 520.0, 530.0, 350.0, 350.0],
        "T0_toolIndex0_temporalRotateRectangle_y_center": [500.0, 515.0, 500.0, 570.0, 510.0, 510.0, 500.0, 620.0, 580.0]
    }
}


TestShapeReducerTemporalRotateRectangleHdbscan = ReducerTest(
    shape_reducer_hdbscan,
    process_data_hdbscan,
    extracted_data,
    processed_data,
    reduced_data_hdbscan,
    'Test shape temporalRotateRectangle reducer with HDBSCAN',
    network_kwargs=kwargs_extra_data,
    pkwargs={'shape': 'temporalRotateRectangle'},
    kwargs={
        'min_cluster_size': 2,
        'allow_single_cluster': True,
        'metric_type': 'IoU',
        'min_samples': 1,
    },
    test_name='TestShapeReducerTemporalRotateRectangleHdbscan',
    round=1,
)
