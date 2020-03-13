from styx_msgs.msg import TrafficLight
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

ckpt_path = '../../../../classifier/model/frozen_inference_graph.pb'

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
    self.detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(ckpt_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
    self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
    self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')

    def load_image_into_numpy_array(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        light = TrafficLight.UNKNOWN
        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                #image = Image.open('../../../classifier/training_data/examples/image11.jpg')
                image_np = self.load_image_into_numpy_array(image)
                image_np_expanded = np.expand_dims(image_np, axis=0)
                (scores, classes) = sess.run([detection_scores, detection_classes],feed_dict={image_tensor: image_np_expanded})

            if np.max(scores) > 0.6:
                light = classes[np.where(scores == np.amax(scores))]

            return light
