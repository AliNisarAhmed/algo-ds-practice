using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp.LeetCode
{
    public static class RomanToInt
    {
        public static int Solution(string s)
        {
            var roman = new Dictionary<Char, int>
            {
                { 'I', 1 },
                { 'V', 5 },
                { 'X', 10 },
                { 'L', 50 },
                { 'C', 100 },
                { 'D', 500 },
                { 'M', 1000 }
            };

            var result = 0;

            var i = 0;
            while (i < s.Length)
            {
                var c = s[i];

                char next = 'z';
                
                if (i + 1 < s.Length)
                {
                    next = s[i + 1];
                    if (c == 'I')
                    {
                        if (next == 'V' || next == 'X')
                        {
                            result += roman[next] - roman[c];
                            i += 2;
                        }
                        else
                        {
                            result += roman[c];
                            i += 1;
                        }
                    }
                    else if (c == 'X')
                    {
                        if (next == 'L' || next == 'C')
                        {
                            result += roman[next] - roman[c];
                            i += 2;
                        }
                        else
                        {
                            result += roman[c];
                            i += 1;
                        }
                    }
                    else if (c == 'C')
                    {
                        if (next == 'D' || next == 'M')
                        {
                            result += roman[next] - roman[c];
                            i += 2;
                        }
                        else
                        {
                            result += roman[c];
                            i += 1;
                        }
                    }
                    else
                    {
                        var value = roman[c];
                        result += value;
                        i++;
                    }
                }
                else
                {
                    var value = roman[c];
                    result += value;
                    i++;
                }
                
                
            }

            return result;
        }
    }
}
