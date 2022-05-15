#include <bits/stdc++.h>

using namespace std;


void quickSort(vector<int> &numbers)
{
    auto startPosition = 1;

    if (numbers.size() <= startPosition)
    {
        return;
    }

    auto pivot = numbers[0];
    auto left = vector<int>();
    auto right = vector<int>();

    // partition
    for (auto index=startPosition; index < numbers.size(); index++)
    {
        auto currentValue = numbers[index];

        if (currentValue < pivot)
        {
            left.push_back(currentValue);
        }
        else
        {
            right.push_back(currentValue);
        }
    }

    // sort partitions
    quickSort(left);
    quickSort(right);

    // combine
    auto position = 0;
    auto delimiter = " ";

    for (auto index=0; index < left.size(); index++)
    {
        numbers[position++] = left[index];
        cout << left[index] << delimiter;
    }

    numbers[position++] = pivot;
    cout << pivot << delimiter;

    for (auto index=0; index < right.size(); index++)
    {
        numbers[position++] = right[index];
        cout << right[index] << delimiter;
    }

    cout << endl;
    return;
}


int main()
{
    int n;
    cin >> n;

    vector <int> arr(n);
    for(int i = 0; i < (int)n; ++i)
    {
        cin >> arr[i];
    }

    quickSort(arr);

    return 0;
}
