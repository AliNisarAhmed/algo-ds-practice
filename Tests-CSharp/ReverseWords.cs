using System;
using System.Collections.Generic;
using System.Text;
using Xunit;
using CSharp.InterviewCake.Arrays;


namespace Tests_CSharp
{
    public class ReverseWordsTest
    {
        [Fact]
        public void OneWordTest()
        {
            var expected = "vault".ToCharArray();
            var actual = "vault".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void TwoWordsTest()
        {
            var expected = "cake thief".ToCharArray();
            var actual = "thief cake".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ThreeWordsTest()
        {
            var expected = "get another one".ToCharArray();
            var actual = "one another get".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void MultipleWordsSameLengthTest()
        {
            var expected = "the cat ate the rat".ToCharArray();
            var actual = "rat the ate cat the".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void MultipleWordsDifferentLengthsTest()
        {
            var expected = "chocolate bundt cake is yummy".ToCharArray();
            var actual = "yummy is cake bundt chocolate".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void EmptyStringTest()
        {
            var expected = "".ToCharArray();
            var actual = "".ToCharArray();
            ReverseInPlace.ReverseWords(actual);
            Assert.Equal(expected, actual);
        }
    }
}
