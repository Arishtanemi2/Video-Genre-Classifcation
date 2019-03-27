"""
Given a folder of images, build our features for training.
"""
import glob
import pickle
from shutil import copyfile

def label_frames(batch, copyimage=True):
    """Label our frames."""
    # Get all our images.
    images = sorted(glob.glob('./datasets/frames/' + str(batch) + '/*'))
    num_images = len(images)

    print("Labelling %d frames." % num_images)

    # Loop through our images and set our labels.
    labeled_images = []
    for image in images:
        # Get the timestamp.
        timestamp = image.replace('.jpg', '').split('/')[-1]
        label=batch
        # Save it.
        labeled_images.append([timestamp, label])
        # Copy it.
        if copyimage:
            copyfile(image, './images/classifications/' + label + '/' + timestamp + '.jpg')


    print("Done labelling!" )
    with open('data/labeled-frames-' + str(batch) + '.pkl', 'wb') as fout:
        pickle.dump(labeled_images, fout)
    return labeled_images

if __name__ == '__main__':
    batches = ['Action','Animation','Horror','Romance','SciFi','Sports']
    for batch in batches:
        label_frames(batch,copyimage=False)
