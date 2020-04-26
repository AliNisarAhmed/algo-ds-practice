using System;
using System.Linq;

public static class JadenCase
{
    public static string ToJadenCase(this string phrase)
    {
        return string.Join(" ", 
            phrase
                .Split(" ")
                .Select(s => s[0].ToString().ToUpper() + s.Substring(1)));
                
    }
}