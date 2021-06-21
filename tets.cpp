#include <algorithm>
#include<iostream>
#include <string>
class Test1;
class Test;


int main()
{
    Test test;
}

class Test
{
    public:
    int x;
    Test1 temp;
    Test()
    {
        x = 10;
        temp = Test1(this);
        temp.out();
    }
};

class Test1
{
    public:
    int y;
    Test1(){y = 0;}
    Test1(Test* test)
    {
        y = test->x;
    }
    void out()
    {
        std::cout << y;
    }
};