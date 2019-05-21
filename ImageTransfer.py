#아직 미완성본! 
#기존에 있던 알고리즘을 사용하여 우리 프로젝트의 목적에 맞게 수정하고 함수 및 코드들을 추가해서 만드는 중


#라이브러러 준비
import os
import cv2
import sys
import numpy as np
import scipy.io
import scipy.misc
import tensorflow as tf  #텐져플로우 라이브러리
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
#%matplotlib inline

#------------이미지 준비 과정
# 완성 이미지 저장공간
OUTPUT_DIR = 'output11/'
# 원하는 스타일의 이미지 이름
STYLE_IMAGE = 'Ss.jpg'
# 원하는 이미지 선택
CONTENT_IMAGE = 'OPENCV (1).jpg'

#이미지 크기 설정
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 400
COLOR_CHANNELS = 3

#오픈CV관련 이미지
img = CONTENT_IMAGE
original = "art.jpg"

#---------openCV과정관련 함수
def combine_two(input1, input2):#두 이미지 결합 함수
    # combine_two( wartershed(img),original)
    # original이 원본 , img = 변한 화면
    # img1 = cv2.imread(input1, -1)#검은배경화면
    # img2 = cv2.imread(input2, -1)#원본사진
    img1 = cv2.imread(input1)
    img2 = cv2.imread(input2)

    # 사진 크기 조절(dsize를 통해 완성 이미지의 사이즈 조절 가능)
    img1 = cv2.resize(img1, dsize=(300, 400))
    img2 = cv2.resize(img2, dsize=(300, 400))


'''
pesudo code!!

배경이 검은색 부분은 이미지 결합시 투명하게 만들어주는 코드를 넣을 생각이다.

'''

    # 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐.
    dst = cv2.add(img1_fg, img2_bg)

    # 합쳐진 이미지를 원본 이미지에 추가.
    img2[0:rows, 0:cols] = dst

    plt.imshow(img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    
    # 중간 파일 제거
    os.remove('middle.jpg')
    # 마지막 파일 저장
    cv2.imwrite('Final.jpg', img2)

#이미지 내의 객체의 Edge를 구별하고 배경을 색칠하는 함수
def wartershed(input_im): 
    img = cv2.imread(input_im) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

'''
pseudo code!!
이미지 내에 객체별로 레이어 값을 붙여 원하는 부분 
즉 원하는 레이어를 선택하여 부분 합성에 이용

'''


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(ret)
    # markers==1 이면 배경
    ret = int(ret)
    for i in range(ret + 1):
        if i != 3:
            img[markers == i] = [0, 0, 0]

    cv2.imwrite('middle.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return "middle.jpg"

#-------------------------IMAGE TRANSFER 조절
NOISE_RATIO = 0.6
BETA = 5
ALPHA = 100
#위에 α/β값이 작아질수록 content보다는 style에 더 치중된 결과

# 다운받은 vgg_ model의 이름을 VGG_MODEL에 넣는다
VGG_MODEL = 'imagenet-vgg-verydeep-19.mat'

#reshape
MEAN_VALUES = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))

#-------------------------IMAGE TRANSFER VGG MODEL 준비
def load_vgg_model(path):
    vgg = scipy.io.loadmat(path)

    vgg_layers = vgg['layers']
    def _weights(layer, expected_layer_name):
        """
        Return the weights and bias from the VGG model for a given layer.
        """
        W = vgg_layers[0][layer][0][0][0][0][0]
        b = vgg_layers[0][layer][0][0][0][0][1]
        layer_name = vgg_layers[0][layer][0][0][-2]
        assert layer_name == expected_layer_name
        return W, b

    def _relu(conv2d_layer):
        """
        Return the RELU function wrapped over a TensorFlow layer. Expects a
        Conv2d layer input.
        """
        return tf.nn.relu(conv2d_layer)

    def _conv2d(prev_layer, layer, layer_name):
        """
        Return the Conv2D layer using the weights, biases from the VGG
        model at 'layer'.
        """
        W, b = _weights(layer, layer_name)
        W = tf.constant(W)
        b = tf.constant(np.reshape(b, (b.size)))
        return tf.nn.conv2d(
            prev_layer, filter=W, strides=[1, 1, 1, 1], padding='SAME') + b

    def _conv2d_relu(prev_layer, layer, layer_name):
        """
        Return the Conv2D + RELU layer using the weights, biases from the VGG
        model at 'layer'.
        """
        return _relu(_conv2d(prev_layer, layer, layer_name))

    def _avgpool(prev_layer):
        """
        Return the AveragePooling layer.
        """
        return tf.nn.avg_pool(prev_layer, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # Constructs the graph model.
    graph = {}
    graph['input']   = tf.Variable(np.zeros((1, IMAGE_HEIGHT, IMAGE_WIDTH, COLOR_CHANNELS)), dtype = 'float32')
    graph['conv1_1']  = _conv2d_relu(graph['input'], 0, 'conv1_1')
    graph['conv1_2']  = _conv2d_relu(graph['conv1_1'], 2, 'conv1_2')
    graph['avgpool1'] = _avgpool(graph['conv1_2'])
    graph['conv2_1']  = _conv2d_relu(graph['avgpool1'], 5, 'conv2_1')
    graph['conv2_2']  = _conv2d_relu(graph['conv2_1'], 7, 'conv2_2')
    graph['avgpool2'] = _avgpool(graph['conv2_2'])
    graph['conv3_1']  = _conv2d_relu(graph['avgpool2'], 10, 'conv3_1')
    graph['conv3_2']  = _conv2d_relu(graph['conv3_1'], 12, 'conv3_2')
    graph['conv3_3']  = _conv2d_relu(graph['conv3_2'], 14, 'conv3_3')
    graph['conv3_4']  = _conv2d_relu(graph['conv3_3'], 16, 'conv3_4')
    graph['avgpool3'] = _avgpool(graph['conv3_4'])
    graph['conv4_1']  = _conv2d_relu(graph['avgpool3'], 19, 'conv4_1')
    graph['conv4_2']  = _conv2d_relu(graph['conv4_1'], 21, 'conv4_2')
    graph['conv4_3']  = _conv2d_relu(graph['conv4_2'], 23, 'conv4_3')
    graph['conv4_4']  = _conv2d_relu(graph['conv4_3'], 25, 'conv4_4')
    graph['avgpool4'] = _avgpool(graph['conv4_4'])
    graph['conv5_1']  = _conv2d_relu(graph['avgpool4'], 28, 'conv5_1')
    graph['conv5_2']  = _conv2d_relu(graph['conv5_1'], 30, 'conv5_2')
    graph['conv5_3']  = _conv2d_relu(graph['conv5_2'], 32, 'conv5_3')
    graph['conv5_4']  = _conv2d_relu(graph['conv5_3'], 34, 'conv5_4')
    graph['avgpool5'] = _avgpool(graph['conv5_4'])
    return graph

#-----------------------------------------CONTENTS 이미지 손실 계산
def content_loss_func(sess, model):
    """
    Content loss function as defined in the paper.
    """
    def _content_loss(p, x):
        # N is the number of filters (at layer l).
        N = p.shape[3]
        # M is the height times the width of the feature map (at layer l).
        M = p.shape[1] * p.shape[2]
        # Interestingly, the paper uses this form instead:
        #
        #   0.5 * tf.reduce_sum(tf.pow(x - p, 2))
        #
        # But this form is very slow in "painting" and thus could be missing
        # out some constants (from what I see in other source code), so I'll
        # replicate the same normalization constant as used in style loss.
        return (1 / (4 * N * M)) * tf.reduce_sum(tf.pow(x - p, 2))
    return _content_loss(sess.run(model['conv4_2']), model['conv4_2'])

#사용할 레이어
STYLE_LAYERS = [
    ('conv1_1', 0.5),
    ('conv2_1', 1.0),
    ('conv3_1', 1.5),
    ('conv4_1', 3.0),
    ('conv5_1', 4.0),
]

#스타일 이미지의 손실계산
def style_loss_func(sess, model):
    """
    Style loss function as defined in the paper.
    """
    def _gram_matrix(F, N, M):
        """
        The gram matrix G.
        """
        Ft = tf.reshape(F, (M, N))
        return tf.matmul(tf.transpose(Ft), Ft)

    def _style_loss(a, x):
        """
        The style loss calculation.
        """
        # N is the number of filters (at layer l).
        N = a.shape[3]
        # M is the height times the width of the feature map (at layer l).
        M = a.shape[1] * a.shape[2]
        # A is the style representation of the original image (at layer l).
        A = _gram_matrix(a, N, M)
        # G is the style representation of the generated image (at layer l).
        G = _gram_matrix(x, N, M)
        result = (1 / (4 * N**2 * M**2)) * tf.reduce_sum(tf.pow(G - A, 2))
        return result

    E = [_style_loss(sess.run(model[layer_name]), model[layer_name]) for layer_name, _ in STYLE_LAYERS]
    W = [w for _, w in STYLE_LAYERS]
    loss = sum([W[l] * E[l] for l in range(len(STYLE_LAYERS))])
    return loss

#------------------------노이지 이미지 생성
def generate_noise_image(content_image, noise_ratio = NOISE_RATIO):
    """
    Returns a noise image intermixed with the content image at a certain ratio.
    """
    noise_image = np.random.uniform(
            -20, 20,
            (1, IMAGE_HEIGHT, IMAGE_WIDTH, COLOR_CHANNELS)).astype('float32')
    # White noise image from the content representation. Take a weighted average
    # of the values
    input_image = noise_image * noise_ratio + content_image * (1 - noise_ratio)
    return input_image

#이미지 저장함수
def load_image(path):
    image = scipy.misc.imread(path)
    # Resize the image for convnet input, there is no change but just
    # add an extra dimension.
    image = np.reshape(image, ((1,) + image.shape))
    # Input to the VGG model expects the mean to be subtracted.
    image = image - MEAN_VALUES
    return image

#이미지 저장 함수
def save_image(path, image):
    # Output should add back the mean.
    image = image + MEAN_VALUES
    # Get rid of the first useless dimension, what remains is the image.
    image = image[0]
    image = np.clip(image, 0, 255).astype('uint8')
    scipy.misc.imsave(path, image)


#----------------------------------텐져플로우 세션 준비
sess = tf.InteractiveSession()

#----------------------------------contents 이미지 준비
content_image = load_image(CONTENT_IMAGE)
imshow(content_image[0]) #애는 콘텐츠 이미지 보여주기 용

#----------------------------------style 이미지 준비

style_image = load_image(STYLE_IMAGE)
imshow(style_image[0]) #애는 스타일 이미지 보여주기 용

#----------------------------------VGG 모델 준비
model = load_vgg_model(VGG_MODEL)

#----------------------------------
print(model) # 생략 가능

#---------------------------------- 콘텐츠에 노이즈 생성

input_image = generate_noise_image(content_image)
imshow(input_image[0]) #보여주기용

#----------------------------------
sess.run(tf.initialize_all_variables())

#----------------------------------
sess.run(model['input'].assign(content_image))
content_loss = content_loss_func(sess, model)

#----------------------------------
# Construct style_loss using style_image.
sess.run(model['input'].assign(style_image))
style_loss = style_loss_func(sess, model)

#----------------------------------
# Instantiate equation 7 of the paper.
total_loss = BETA * content_loss + ALPHA * style_loss
#----------------------------------
optimizer = tf.train.AdamOptimizer(2.0)
train_step = optimizer.minimize(total_loss)
#----------------------------------
sess.run(tf.initialize_all_variables())
sess.run(model['input'].assign(input_image))

#---------------------------------- 반복 횟수 지정
ITERATIONS = 1000

#---------------------------------- 반복 시작------------------------------------
sess.run(tf.initialize_all_variables())
sess.run(model['input'].assign(input_image))
for it in range(ITERATIONS):
    sess.run(train_step)
    if it%100 == 0:
        # Print every 100 iteration.
        mixed_image = sess.run(model['input'])
        print('Iteration %d' % (it))
        print('sum : ', sess.run(tf.reduce_sum(mixed_image)))
        print('cost: ', sess.run(total_loss))

        if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

        filename = 'output11/%d.png' % (it) # OUPUT11이라는 이름의 파일에 저장
        save_image(filename, mixed_image)


 # ---------------------------------- 이미지 변화된 사진 저장-----
save_image('art.jpg', mixed_image)

# ---------------------------------- 위에 art.jpg를 이용하여 부분 합성 시작
combine_two(wartershed(img),original)
