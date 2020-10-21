from __future__ import print_function

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# Create a Constant op
hello = tf.constant('Hello, World!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))
