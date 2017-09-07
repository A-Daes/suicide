#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;



int main( int argc, char** argv )
{
    if( argc != 2)
    {
     cout <<" Usage: display_image ImageToLoadAndDisplay" << endl;
     return -1;
    }

    Mat image;
    Mat grsc;
    image = imread(argv[1], CV_LOAD_IMAGE_COLOR);   // Read the file
    grsc = imread(argv[1], CV_LOAD_IMAGE_GRAYSCALE ); 
    Size S = grsc.size();
                     
    // Check for invalid input

    if(! image.data )   
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }

    namedWindow( "Display window", WINDOW_AUTOSIZE );// Create a window for display.
    namedWindow( "Grayscale", WINDOW_AUTOSIZE); 
    moveWindow( "Grayscale", S.width + 64, 0 );
    imshow( "Grayscale", grsc);
    imshow( "Display window", image );                   // Show our image inside it.

    waitKey(0);                                          // Wait for a keystroke in the window
    return 0;
}

