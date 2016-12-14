import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data
"""Tensorflow import"""

# Dataset loading
mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)

# Set up model
x = tf.placeholder(tf.float32, [None, 784]) 
'''계산을 하도록 명령할 때 입력할 값 '''
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10])) 
'''0으로 채워진 텐서들로 초기화'''
y = tf.nn.softmax(tf.matmul(x, W) + b)
'''x 곱하기 W 다음 b를 더하고, tf.nn.softmax 적용'''
y_ = tf.placeholder(tf.float32, [None, 10]) 
'''교차 엔트로피를 구현하기 위한 정답을 입력하기 위한 새 placeholder 추가   '''

cross_entropy = -tf.reduce_sum(y_*tf.log(y)) 
''' 교차 엔트로피 구현 '''
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) 
'''역전파 알고리즘을 이용하여 비용최소화에 대산 변수의 영향을 효율적으로 구한다. '''

# Session
init = tf.initialize_all_variables()
'''실행전 변수들 초기화'''
sess = tf.Session()
sess.run(init)
'''모델시작하고 변수들을 초기화 하는 작업을 실행'''

# Learning
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  '''학습을 1000번 돌림 placeholders를 대체하기 위한 일괄 처리 데이터에 train_step 피딩을 실행합니다.'''

# Validation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
'''tf.argmax는 특정한 축을 따라 가장 큰 원소의 색인을 알려주는 함수, tf.equal 을 이용해 예측이 실제와 맞았는지 확인,결과로 부울 리스트를 받음'''
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
'''부정소숫점으로 캐스팅한 후 평균값을 구하면 맞은 비율을 구할수 있다.'''

# Result should be approximately 91%.
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
'''정확도 확인'''
