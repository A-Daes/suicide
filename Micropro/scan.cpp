//Lab 2
//Universidad del Valle de Guatemala
//Christian Medina Armas


#include <opencv2/core.hpp>
#include <opencv2/core/utility.hpp>
#include "opencv2/imgcodecs.hpp"
#include <opencv2/highgui.hpp>
#include <iostream>
#include <sstream>

#define N 100

using namespace std;
using namespace cv;


//function prototypes
Mat& scanImage(Mat&, int);

int main( int argc, char *argv[]){

    if (argc < 3){
        cout<< "Not enough arguments"<< endl;
        return -1;
    }

    //declare image conainers
    Mat source, result;
    
    //load image
    //c parameter has to be addded for color images
    ( !strcmp(argv[2],"c") ? source = imread(argv[1], IMREAD_COLOR) : source = imread(argv[1], IMREAD_GRAYSCALE) );

    //test image contents
    if(source.empty()){
        cout << "The image" << argv[1] << " could not be loaded." << endl;
	return -1;
    }


    double t;

    //start time measure
    t = (double)getTickCount();

    //loop N times for exec-time calc
    for (int i=0; i<N ; i++){
	//create a copy of the source image
        Mat src_tmp = source.clone();

	//apply the operator
        result = scanImage(src_tmp, 10);
    }

    //compute exec-time
    t = 1000*((double)getTickCount() - t)/getTickFrequency();
    t /= N;

    cout << "Avg time for "<< N << " runs: " << t << " ms."<< endl;

  return 0;
}



//-----------------------------------------------------------
//
//-----------------------------------------------------------
Mat& scanImage(Mat& input, int k){

    //verify that the pixels are type CV_8U AKA 8-bit unsigned integers  0..255)
    CV_Assert(input.depth() == CV_8U);

    //get number of channels
    IMREAD_GRAYSCALE = 1
    IMREAD_COLOR = 3
    int channels = input.channels();

    int rows = input.rows;
    int cols = input.cols * channels;

    //test if image is stored in a continous memory space
    if (input.isContinuous()){
        cols *= rows;
        rows = 1;
    }


    switch(channels){

    case 1:{
        //declare pointer
        uchar* p;

        for( int i=0; i<rows; ++i){

	    //get pointer to image
            p = input.ptr<uchar>(i);

            for (int j=0; j<cols; ++j){
                p[j] = p[j] + k;
            }
        }
    }
    case 3:{
	//your code goes here
    }

    } 
    return input;
}
//-----------------------------------------------------------
