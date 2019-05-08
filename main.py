import extension
import canny_edge_detector as ced

def main():
    img = extension.load_data()
    extension.visualize(img, 'gray')

    detector = ced.cannyEdgeDetector(img, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
    final_img = detector.detect()

    extension.visualize(final_img, 'gray')

if __name__ == '__main__':
    main()