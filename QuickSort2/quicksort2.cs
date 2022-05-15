using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;


class Solution
{
    static void quickSort(List<int> numbers)
    {
        var startPosition = 1;

        if (numbers.Count <= startPosition)
        {
            return;
        }

        var pivot = numbers[0];
        var splitSize = numbers.Count/2;
        var left = new List<int>(splitSize);
        var right = new List<int>(splitSize);

        // partition
        foreach(var number in numbers.Skip(startPosition))
        {
            if (number < pivot)
            {
                left.Add(number);
            }
            else
            {
                right.Add(number);
            }
        }

        // sort partitions
        quickSort(left);
        quickSort(right);

        // combine
        var position = 0;

        for(var index=0; index < left.Count; index++)
        {
            numbers[position++] = left[index];
        }

        numbers[position++] = pivot;

        for(var index=0; index < right.Count; index++)
        {
            numbers[position++] = right[index];
        }

        var text = string.Join(" ", numbers);
        Console.WriteLine(text);
    }

/* Tail starts here */
    static void Main(String[] args)
    {
        int _ar_size;
        _ar_size = Convert.ToInt32(Console.ReadLine());
        int [] _ar = new int [_ar_size];
        String elements = Console.ReadLine();
        String[] split_elements = elements.Split(' ');

        for(int _ar_i=0; _ar_i < _ar_size; _ar_i++)
        {
            _ar[_ar_i] = Convert.ToInt32(split_elements[_ar_i]);
        }

        var numberList = new List<int>(_ar);

        quickSort(numberList);
    }
}
