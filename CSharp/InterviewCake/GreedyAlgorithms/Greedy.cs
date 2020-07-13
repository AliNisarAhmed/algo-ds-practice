﻿using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using Microsoft.VisualBasic;

namespace CSharp.InterviewCake.GreedyAlgorithms
{
    public static class Greedy
    {
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
    }
}
