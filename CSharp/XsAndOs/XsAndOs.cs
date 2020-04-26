using System.Linq;
using System;
using System.Collections.Generic;

public static class Kata
{
    public static bool XO(string input) =>
        input.ToLower().Count(c => c == 'x') == input.ToLower().Count(c => c == 'o');
}