#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'isBalanced' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

struct bracketRule
{
    char start;
    char end;

    bracketRule(char start, char end)
            : start(start)
            , end(end)
    {
    }
};


typedef std::map<char, char> bracketMap;


class BracketValidator
{
    bracketMap startBrackets;
    bracketMap endBrackets;

    bool isStartBracket(char letter)
    {
        return startBrackets.find(letter) != startBrackets.end();
    }

    bool isEndBracket(char letter)
    {
        return endBrackets.find(letter) != endBrackets.end();
    }

    bool isAnyBracket(char letter)
    {
        return isStartBracket(letter) || isEndBracket(letter);
    }

    char getEndBracket(char bracket)
    {
        return startBrackets[bracket];
    }

    char getStartBracket(char bracket)
    {
        return endBrackets[bracket];
    }

public:

    BracketValidator()
    {
    }

    BracketValidator(vector<bracketRule> bracketRules)
    {
        this->addRules(bracketRules);
    }

    void addRule(bracketRule rule)
    {
        startBrackets[rule.start] = rule.end;
        endBrackets[rule.end] = rule.start;
    }

    void addRules(vector<bracketRule> bracketRules)
    {
        for (auto rule: bracketRules)
        {
            startBrackets[rule.start] = rule.end;
            endBrackets[rule.end] = rule.start;
        }
    }

    bool validateBrackets(string text)
    {
        auto isValid = false;
        auto trackedBrackets = std::stack<char>();

        for (char const &letter: text)
        {
            if (trackedBrackets.empty() && this->isAnyBracket(letter))
            {
                trackedBrackets.push(letter);
            }
            else if (this->isStartBracket(letter))
            {
                trackedBrackets.push(letter);
            }
            else if (this->isEndBracket(letter))
            {
                auto bracket = trackedBrackets.top();
                auto startBracket = this->getStartBracket(letter);

                if (bracket == startBracket)
                {
                    trackedBrackets.pop();
                }
                else
                {
                    break;
                }
            }
        }

        if (trackedBrackets.empty())
        {
            isValid = true;
        }

        return isValid;
    }
};


class DefaultBracketValidator
{
public:
    static bool validate(string text)
    {
        const bracketRule curly = bracketRule
                (
                        '{'
                        , '}'
                );

        const bracketRule parenthesis = bracketRule
                (
                        '('
                        , ')'
                );

        const bracketRule squareBracket = bracketRule
                (
                        '['
                        , ']'
                );

        const vector<bracketRule> rules = vector<bracketRule>
                (
                        {
                                curly
                                , parenthesis
                                , squareBracket
                        }
                );

        BracketValidator validator(rules);
        return validator.validateBrackets(text);
    }
};


string getResult(bool result)
{
    const string NO = "NO";
    const string YES = "YES";
    return result ? YES : NO;
}


string isBalanced(string text)
{
    bool areBracketsBalanced = DefaultBracketValidator::validate(text);
    string result = getResult(areBracketsBalanced);
    return result;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
            s.begin(),
            find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
            find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
            s.end()
    );

    return s;
}
