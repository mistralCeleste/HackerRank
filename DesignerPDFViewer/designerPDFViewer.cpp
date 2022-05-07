using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;


class Result
{
    /*
     * Complete the 'designerPdfViewer' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY heights
     *  2. STRING word
     */

    public static readonly int characterWidth = 1;
    public static readonly int characterArrayOffset = 'a';

    public static int designerPdfViewer(List<int> letterHeights, string word)
    {
        var tallestLetter = FindTallestLetter(letterHeights, word);
        var highlightArea = CalculateAreaOfHighlight(tallestLetter, word);
        return highlightArea;
    }

    protected static int CalculateAreaOfHighlight(int height, string word)
    {
        var lengthOfWord = word.Length;
        return Result.characterWidth * lengthOfWord * height;
    }

    protected static int FindTallestLetter(List<int> letterHeights, string word)
    {
        var tallestLetter = 0;

        foreach(var letter in word)
        {
            var letterHeight = GetLetterHeight(letterHeights, letter);
            tallestLetter = GetTaller(tallestLetter, letterHeight);
        }

        return tallestLetter;
    }

    protected static int GetLetterHeight(List<int> letterHeights, char letter)
    {
        int letterOffset = letter - Result.characterArrayOffset;
        return letterHeights[letterOffset];
    }

    protected static bool IsTaller(int value, int comparison)
    {
        return value > comparison;
    }

    protected static int GetTaller(int value, int comparison)
    {
        return IsTaller(value, comparison) ? value : comparison;
    }
}


class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        List<int> h = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(hTemp => Convert.ToInt32(hTemp)).ToList();

        string word = Console.ReadLine();

        int result = Result.designerPdfViewer(h, word);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
