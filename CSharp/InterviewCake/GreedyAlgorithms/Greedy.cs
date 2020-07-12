using System;
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
    }
}
