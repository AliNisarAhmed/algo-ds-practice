using CSharp.InterviewCake.GreedyAlgorithms;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class AppleStocksTest
    {
        [Fact]
        public void PriceGoesUpThenDownTest()
        {
            var actual = Greedy.AppleStocks(new int[] { 1, 5, 3, 2 });
            var expected = 4;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void PriceGoesDownThenUpTest()
        {
            var actual = Greedy.AppleStocks(new int[] { 7, 2, 8, 9 });
            var expected = 7;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void PriceGoesUpAllDayTest()
        {
            var actual = Greedy.AppleStocks(new int[] { 1, 6, 7, 9 });
            var expected = 8;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void PriceGoesDownAllDayTest()
        {
            var actual = Greedy.AppleStocks(new int[] { 9, 7, 4, 1 });
            var expected = -2;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void PriceStaysTheSameAllDayTest()
        {
            var actual = Greedy.AppleStocks(new int[] { 1, 1, 1, 1 });
            var expected = 0;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ExceptionWithOnePriceTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.AppleStocks(new int[] { 5 }));
        }

        [Fact]
        public void ExceptionWithEmptyPricesTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.AppleStocks(new int[] { }));
        }
    }
}
