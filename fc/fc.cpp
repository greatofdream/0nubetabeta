#include "TFeldmanCousins.h"
#include "TMath.h"
extern "C" {
double fc(double bkg, double observed){
    TFeldmanCousins fc1;
    int upper = bkg+5*(int(sqrt(bkg))+1);
    if (upper<50){
        upper = 50;
    }
    fc1.SetMuMax(2*upper);
    double ul = fc1.CalculateUpperLimit(observed, bkg);
    double ll = fc1.GetLowerLimit();
    return ul;
}

double fcAvg(double bkg){
    //fmuMax=50 in TFeldmanCousins Class
    double sensitivity = 0;
    int upper = bkg+5*(1+int(sqrt(bkg)));
    if (upper<50){
        upper = 50;
    }
    for(int i=0;i<upper;i++){
        sensitivity += TMath::Poisson(i, bkg)*fc(bkg,i);
    }
    return sensitivity;
}
}