import tensorflow as tf
import numpy as np

#자료형 설정 ex) [여성, 남성]
x_data = np.array([
    [1, 0], 
    [0, 0], 
    [1, 1], 
    [0, 1], 
    [1, 1], 
    [0, 1]])
#자료형 설정 ex) [유아기, 청년기, 장년기]    
y_data = np.array([
    [0, 0, 0], 
    [0, 0, 1], 
    [0, 0, 0], 
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]])

#플레이스홀더 설정
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#가중치와 편향값 설정
W = tf.Variable(tf.random_uniform([2, 3], -1., 1.))
b = tf.Variable(tf.zeros([3]))

#활성화 함수 설정
Relu = tf.add(tf.matmul(X, W), b)
Relu = tf.nn.relu(Relu)

#출력값 다듬기 -> softmax결과값들의 전체 합이 1
model = tf.nn.softmax(Relu)
'''
비용함수 설정
교차엔트로피(Cross Entropy) 함수를 사용 - 예측값과 실제값 사이의 확률 분포 차이를 계산해주는 함수
(a) tf.log()함수를 이용해 model 값에 로그를 취한 후 Y를 곱해줍니다.
(b) reduce_sum() 함수를 이용해 각 데이터의 행별로 값을 더해줍니다.
(c) reduce_mean() 함수를 이용해 배열 안 값의 평균을 내줍니다.
'''
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis = 1))

#경사하강법으로 최적화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(cost)

#세션 초기화
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#학습을 200번 진행
for step in range(200):
    sess.run(train_op, feed_dict={X: x_data, Y: y_data})

    # 학습 50번당 1번씩 손실값을 출력
    if (step + 1) % 50 == 0:
        print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))
'''
학습결과 확인
여기서 tf.argmax() 함수는 원 핫 인코딩 형태의 데이터에 최적화된 함수, 지정된 배열에서 가장 큰 값의 인덱스를 반환하는 함수
축(Axis)값에 0을 주면 1차원 배열에 대해 함수를 적용하며
여기서는 1을 주었으므로 2차원 배열에 대해 적용
'''
predict = tf.argmax(model, axis=1)
actval = tf.argmax(Y, axis=1)
print("예상:", sess.run(predict, feed_dict={X: x_data}))
print("실제:", sess.run(actval, feed_dict={Y: y_data}))
'''
정확도 출력
tf.equal() 함수는 두 값이 동일하면 True, 다르면 False를 반환하는 함수
tf.cast() 함수는 True/False 형태의 값을 1과 0으로 바꾸어주는 함수
'''
corr = tf.equal(predict, actval)
accu = tf.reduce_mean(tf.cast(corr, tf.float32))
print("Accuracy: %.2f" % sess.run(accu * 100, feed_dict={X: x_data, Y: y_data}))