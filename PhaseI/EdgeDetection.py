#Laplacian  method
import cv2 as  cv

def  main():
    '''
        Apply Laplacian method to grayscale image and return it

    '''
    #variables
    kernel_size = 3
    ddepth = cv.CV_16S
    window_name =  'Edge Detection'

    #load image  (use your own )
    image = cv.imread('/Users/user/Desktop/CV/images/image 3.webp',cv.IMREAD_COLOR)

    #remove noise
    rnoise_image = cv.GaussianBlur(image,(3,3),0)

    #grayscale
    gray_image = cv.cvtColor(rnoise_image,cv.COLOR_BGR2GRAY)

    #Window
    cv.namedWindow(window_name,cv.WINDOW_AUTOSIZE)
    #laplacian application
    dst = cv.Laplacian(gray_image,ddepth,ksize=kernel_size)

    #change to uint8
    abs_dst = cv.convertScaleAbs(dst)

    cv.imshow(window_name,abs_dst)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
