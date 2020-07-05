using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

namespace CSharp.InterviewCake.HashTables
{
    public static class HashTableClass
    {
        public static bool InFlight(int[] movieLengths, int flightLength)
        {
            // returns if there are two numbers in array whose sum = flightLength

            var dict = new HashSet<int>();

            foreach(var movie in movieLengths)
            {
                if (dict.Contains(flightLength - movie))
                {
                    return true;
                }
                
                else
                {
                    dict.Add(movie);
                }
            }

            return false;
        }
    
        public static bool InFlight_Sorted(int[] movieLengths, int flightLength)
        {
            var i = 0;
            var j = movieLengths.Length - 1;

            while (i < j)
            {
                if (movieLengths[i] + movieLengths[j] == flightLength)
                {
                    return true;
                }
                else if (movieLengths[i] + movieLengths[j] < flightLength)
                {
                    i++;
                }
                else
                {
                    j--;
                }
            }

            return false;
        }
    
        public static bool CheckPalindrome(string input)
        {
            // the idea here is to see if all the characters in the input string appear even number of times
                 // apart from maybe one character which may appear an odd number of times

            // we could use a Dictionary to hold the count of each character.
            // But, using a set, we can add chars to it, if an element is already in there we remove it.
            // by the end, if we have two or more characters still remainin in the set, then we do not have a palindrom.

            var set = new HashSet<char>();

            foreach(var c in input)
            {
                if (set.Contains(c))
                {
                    set.Remove(c);
                }
                else
                {
                    set.Add(c);
                }
            }

            return set.Count <= 1;
        }

        public static Dictionary<string, int> WordCloudData(string input)
        {
            var result = new Dictionary<string, int>();

            var words = SplitWords(input);

            foreach (var item in words)
            {
                int currentCount;

                if (result.TryGetValue(item, out currentCount))
                {
                    result[item] = currentCount + 1;
                }
                else if (result.TryGetValue(item.ToLower(), out currentCount))
                {
                    result[item] = currentCount + 1;
                }
                else if (result.TryGetValue(Capitalize(item), out currentCount))
                {
                    result.Add(item, currentCount + 1);
                    result.Remove(item.ToLower());
                }
                else
                {
                    result.Add(item, 1);
                }

            }

            return result;
        }

        public static string Capitalize(string input)
            => input.Substring(0, 1).ToUpper() + input.Substring(1);
        

        public static List<string> SplitWords(string input)
        {
            var start = 0;
            var wordLength = 0;

            var result = new List<string>();

            for(var i = 0; i < input.Length; i++)
            {
                var c = input[i];

                if (char.IsLetter(c) || c == '\'' || c == '-' || c == '.')
                {
                    wordLength++;
                }
                else
                {
                    // reached word boundary
                    result.Add(input.Substring(start, wordLength));
                    start = i;
                    wordLength = 0;
                }
            }

            return result;
        }
    
        
        
        // Top Scores

        public static int[] SortScores(int[] scores, int highestPossibleScore)
        {
            // 1 - Start with an array for each possible score (0 - highestPossibleScore)
            // and initialize the counts to 0

            var allScores = new int[highestPossibleScore + 1];

            foreach(var score in scores)
            {
                // 2 - since we have an array of 0..100, each score can be found at the index equal to its value, so 
                    // 0 is at index 0, 37 is @ index 37 etc, hence we can increment count easily
                allScores[score]++;
            }

            // Initiate the results array
            int[] sortedScores = new int[scores.Length];
            int currentSortedIndex = 0;

            // 3 - now loop down from highest score one by one...
            // the only task we do is add each number times indicated by its count

            for (var num = highestPossibleScore; num >= 0; num--)
            {
                var count = allScores[num];

                for (var timesInserted = 0; timesInserted < count; timesInserted++)
                {
                    sortedScores[currentSortedIndex] = num;
                    currentSortedIndex++;
                }
            }

            return sortedScores;
        }
    }
}
