#include <iostream>
using namespace std;

const double pi=3.1416;
const int radius=2;

void Area (double radius, double result)
{
    result=pi*radius*radius;
}

int main(){

double AreaFetched=0;
Area(radius, AreaFetched);

cout << "This area is: " <<  AreaFetched << endl;
}
