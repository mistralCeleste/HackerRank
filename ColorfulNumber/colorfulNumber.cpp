#include <iostream>
#include <bits/stdc++.h>

using namespace std;

/*
    Objective: Given a number, find out whether it's colorful or not.

    Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

    Example:

    Given Number : 3245
    Output : Colorful
            Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
    this number is a colorful number, since product of every digit of a sub-sequence are different.
    That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

    Given Number : 326
    Output : Not Colorful.
    326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
    Reference : http://www.careercup.com/question?id=4863869499473920
*/
vector<int>* splitNumber(int value, int base)
{
    auto splitNumbers = new vector<int>();

    for (auto remaining=value; remaining > 0; remaining /= base)
    {
        auto mod = remaining % base;
        splitNumbers->insert(splitNumbers->begin(), mod);
    }

    return splitNumbers;
}


bool createColorMap(vector<int> const *values, map<int, int> *colorMap)
{
    for (auto value: *values)
    {
        if (colorMap->count(value))
        {
            return false;
        }

        (*colorMap)[value] = value;
    }

    return true;
}


bool checkForColor(int value)
{
    auto base = 10;
    auto combinations = splitNumber(value, base);
    auto colorMap = new map<int, int>();

    if (!createColorMap(combinations, colorMap))
    {
        return false;
    }

    for (auto first=0; first < combinations->size(); first++)
    {
        for (auto second=first+1; second < combinations->size(); second++)
        {
            auto firstValue = combinations->at(first);
            auto secondValue = combinations->at(second);
            auto factor = firstValue * secondValue;

            if (colorMap->count(factor))
            {
                return false;
            }

            (*colorMap)[factor] = first;
        }
    }

    return true;
}

int main()
{
    auto exit_code = 0;
    auto testNumbers = map<int, bool>
            (
                    {
                            {11, false}
                            , {326, false}
                            , {3245, true}
                    }
            );

    for (auto testNumber: testNumbers)
    {
        bool isColorful = checkForColor(testNumber.first);
        string result = isColorful ? "Yes" : "No";
        std::cout << result << "\n";

        if (isColorful != testNumber.second)
        {
            exit_code |= 1;
        }
    }

    return exit_code;
}
