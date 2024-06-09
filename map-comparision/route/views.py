from re import template

from django.shortcuts import render
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Post
from .forms import PostForm
from PIL import Image
import cv2
import glob
import numpy as np
from django.http import HttpResponse


    
class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')


def index(request):
    model = Post
    
    img = cv2.imread("media/images/actual.png")
    img1 = cv2.imread("media/images/expected.png")
    crop = img[0:764, 70:1365]
    crop1 = img1[0:764, 70:1365]
    cv2.imwrite("media/images/actual/actual.png",crop)
    cv2.imwrite("media/images/expected/expected.png",crop1)
    

    
        


    # for filename in glob.glob('media/images/expected/*.png'):
    #reading map images
    expected_route_img = cv2.imread('media/images/expected/expected.png') 


    #converting BGR TO HSV
    hsv = cv2.cvtColor(expected_route_img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([50, 192, 160])
    upper_blue = np.array([70, 255, 255])


    # defining range of bluecolor in HSV, This creates a mask of blue coloured route found in the frame.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(mask, kernel, iterations=1)
    cv2.imwrite('media/images/expected/expected.png', img_dilation)

    #storing converted image
        



    # for filename in glob.glob('media/images/actual/*.png'):

    #reading map images
    actual_route_img = cv2.imread('media/images/actual/actual.png') 


    #converting BGR TO HSV
    hsv = cv2.cvtColor(actual_route_img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([0,0,0])
    upper_blue = np.array([0,0,0])


    # defining range of bluecolor in HSV, This creates a mask of blue coloured route found in the frame.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(mask, kernel, iterations=1)
    cv2.imwrite('media/images/actual/actual.png', img_dilation)


    
        

    # for i,j in zip(glob.glob('media/images/actual/*.png'),glob.glob('media/images/expected/*.png')):
    matched=[] #list for storing matched pixel of route
    white_in_original_route=[] #list for storing original route 
    taking_route = Image.open('media/images/actual/actual.png','r')
    original_route= Image.open('media/images/expected/expected.png','r')


        #fetching pixel 
    pix_val_taking = list(taking_route.getdata())
    pix_val_original = list(original_route.getdata())

        #matching pixel of taking_route and original_route
    for a,b in zip(pix_val_taking,pix_val_original):
        if  a!=0 and a==b and b!=0:
            matched.append(a)

        #finding original route pixel from map image
    for ii in pix_val_original:
        if ii!=0:
            white_in_original_route.append(ii)

        #calculating percentage of matching route
    output = (100-((len(matched)/len(white_in_original_route))*100))
    return render(request, "home.html", {'result': output})



    

# Create your views here.
