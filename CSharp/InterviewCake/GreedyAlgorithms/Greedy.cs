using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using Microsoft.VisualBasic;

namespace CSharp.InterviewCake.GreedyAlgorithms
{
    public static class Greedy
    {
        private static Random _rand = new Random();

        public static int AppleStocks(int[] stockPrices)
        {
            if (stockPrices.Length <= 1)
                throw new ArgumentException();

            //var currentMin = int.MaxValue;
            //var max = int.MinValue;

            var currentMin = stockPrices[0];
            var max = stockPrices[1] - stockPrices[0];

            for (var i = 1; i < stockPrices.Length; i++)
            {
                var currentPrice = stockPrices[i];

                var difference = currentPrice - currentMin;

                max = Math.Max(difference, max);

                currentMin = Math.Min(currentMin, currentPrice);
            }

            return max;
        }
    
        
        public static int HighestProductOf3(int[] inputs)
        {
            if (inputs.Length < 3)
                throw new ArgumentException();

            var result = inputs[0] * inputs[1] * inputs[2];
            var highest2 = inputs[0] * inputs[1];
            var lowest2 = inputs[0] * inputs[1];
            var max = Math.Max(inputs[0], inputs[1]);
            var min = Math.Min(inputs[0], inputs[1]);

            for (var i = 2; i < inputs.Length; i++)
            {
                var current = inputs[i];

                if (highest2 * current > result)
                {
                    result = highest2 * current;
                }

                if (lowest2 * current > result)
                {
                    result = lowest2 * current;
                }

                if (max * current > highest2)
                {
                    highest2 = max * current;
                }

                if (max * current < lowest2)
                {
                    lowest2 = max * current;
                }

                if (current > max)
                {
                    max = current;
                }

                if (min * current < lowest2)
                {
                    lowest2 = min * current;
                }

                if (min * current > highest2)
                {
                    highest2 = min * current;
                }

                if (current < min)
                {
                    min = current;
                }
            }

            return result;
        }
    
        
        public static int[] GetProductsOfAllIntsExceptAtIndex(int[] input)
        {
            if (input.Length <= 1)
                throw new ArgumentException("Input cannot contain 1 or less elements");

            var result = new int[input.Length];

            var productSoFar = 1;
            for (var i = 0; i < input.Length; i++)
            {
                result[i] = productSoFar;
                productSoFar *= input[i];
            }

            productSoFar = 1;
            for (var i = input.Length - 1; i >= 0; i--)
            {
                result[i] *= productSoFar;
                productSoFar *= input[i];
            }

            return result;
        }
    
        
        public static void Shuffle(int[] input)
        {
            if (input.Length <= 1)
                return;

            for (var i = 0; i < input.Length; i++)
            {
                var randomIndex = GetRandom(i, input.Length - 1);

                if (randomIndex != i)
                {
                    var temp = input[randomIndex];
                    input[randomIndex] = input[i];
                    input[i] = temp;
                }
            }
        }


        public static int GetRandom(int floor, int ceil)
        {
            return _rand.Next(floor, ceil + 1);
        }
    }
}
