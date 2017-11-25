#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

class Animal{
    public:
        virtual void makeSound(){ cout << "The Animal says grr" << endl; }

};

class Dog : public Animal{
    public:
        void makeSound(){ cout << "The Dog says woof" << endl;}
    
};

class Cat : public Animal{
    public:
         void makeSound(){ cout << "The Cat says meow" << endl;}
};

class Car{
    public:
        virtual int getNumWheels() = 0;
        virtual int getNumDoors() = 0;
        
};

class StationWagon : public Car{
    public: 
        int getNumWheels(){ cout << "Station wagon has 4 wheels" << endl;}
        int getNumDoors(){ cout << "Station wagon has 4 doors" << endl;}
        StationWagon() {}
        ~StationWagon();
};

int main(){
    Animal* pCat = new Cat;
    Animal* pDog = new Dog;
    
    pCat -> makeSound();
    pDog -> makeSound();
    
    Car* stationWagon = new StationWagon();
    
    stationWagon -> getNumWheels();
    
    
    return 0;
}


