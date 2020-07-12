using CSharp.InterviewCake.HashTables;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class InFlight
    {

        [Fact]
        public void ShortFlightTest()
        {
            var result = HashTableClass.InFlight(new int[] { 2, 4 }, 1);
            Assert.False(result);
        }

        [Fact]
        public void LongFlightTest()
        {
            var result = HashTableClass.InFlight(new int[] { 2, 4 }, 6);
            Assert.True(result);
        }

        [Fact]
        public void OnlyOneMovieHalfFlightLenghtTest()
        {
            var result = HashTableClass.InFlight(new int[] { 3, 8 }, 6);
            Assert.False(result);
        }

        [Fact]
        public void TwoMoviesHalfFlightLengthTest()
        {
            var result = HashTableClass.InFlight(new int[] { 3, 8, 3 }, 6);
            Assert.True(result);
        }

        [Fact]
        public void LotsOfPossiblePairsTest()
        {
            var result = HashTableClass.InFlight(new int[] { 1, 2, 3, 4, 5, 6 }, 7);
            Assert.True(result);
        }

        [Fact]
        public void NotUsingFirstMovieTest()
        {
            var result = HashTableClass.InFlight(new int[] { 4, 3, 2 }, 5);
            Assert.True(result);
        }

        [Fact]
        public void OneMovieTest()
        {
            var result = HashTableClass.InFlight(new int[] { 6 }, 6);
            Assert.False(result);
        }

        [Fact]
        public void NoMoviesTest()
        {
            var result = HashTableClass.InFlight(new int[] { }, 6);
            Assert.False(result);
        }
    }
}
