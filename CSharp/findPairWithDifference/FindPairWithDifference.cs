using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharp
{
  public static class FindPairWithDifference
  {
    public static IEnumerable<Tuple<int, int>> FindPair(int[] nums, int diff)
    {
      IEnumerable<Tuple<int, int>> result = new List<Tuple<int, int>>();
      var dict = new Dictionary<int, List<Tuple<int, int>>>();
      foreach (var n in nums)
      {
        if (dict.ContainsKey(n - 2))
        {
          dict[n - 2].Add(new Tuple<int, int>(n - 2, n));
        }
        else if (dict.ContainsKey(n + 2))
        {
          dict[n + 2].Add(new Tuple<int, int>(n + 2, n));
        }
        else if (!dict.ContainsKey(n))
        {
          dict[n] = new List<Tuple<int, int>>();
        }

      }

      foreach (var v in dict.Values)
      {
          result = result.Concat(v);
      }

      return result;
    }
  }

}