#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(){
    cout << "Hello World!!!" << endl;
    
    const double PI = 3.1415926535;
    
    char myGrade = 'A';
    
    bool isHappy = true;
    
    int myAge = 39;
    
    float favNum = 3.141592;
    
    double otherfavNum = 1.6180339887;
    
    cout << "Favorite Number " << favNum << endl;
    
    cout << "Size of int " << sizeof(myAge) << endl;
    
    int largestInt = 2147483647;
    
    cout << "Largest int " << largestInt << endl;
    
    int five = 5;
    
    cout << "5++ = " << five++ << endl;
    cout << "++5 = " << ++five << endl;
    
    cout << "4 / 5 = " << 4 / 5 << endl;
    cout << "4 / 5 = " << (float)4 / 5 << endl;
    
    int age = 70;
    int ageAtLastExam = 16;
    bool isNotIntoxicated = true;
    
    if( (age >= 1) && (age < 16) ){
        cout << "You can't drive" << endl;
    } else if(! isNotIntoxicated){
        cout << "You can't drive" << endl;
    } else if(age >= 80 && ( (age > 100) || ( (age - ageAtLastExam) > 5) ) ) {
        cout << "You can't drive" << endl;
    } else {
        cout << "You can drive" << endl;
    }
    
    return 0;
}
