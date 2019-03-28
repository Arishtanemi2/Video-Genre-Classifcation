"""
Given a single image, predict it's genre
"""
import sys
import tensorflow as tf

def get_labels():
    """Get the  list of labels"""
    with open('./inception/retrained_labels.txt', 'r') as fin:
        labels = [line.rstrip('\n') for line in fin]
        return labels

def predict_on_image(image):
    """Given an image, predict its class."""
    labels = get_labels()

    # Unpersists graph from file
    with tf.gfile.FastGFile("./inception/retrained_graph.pb", 'rb') as fin:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fin.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image, 'rb').read()

        try:
            predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
            prediction = predictions[0]
        except:
            print("Error making prediction.")
            sys.exit()

        # List of predictions. See retrained_labels.txt for labels.
        print(prediction)
        prediction = prediction.tolist()
        max_value = max(prediction)
        max_index = prediction.index(max_value)
        predicted_label = labels[max_index]
        print(predicted_label)

if __name__ == '__main__':
    dir=input("enter image location:")
    predict_on_image(dir)
