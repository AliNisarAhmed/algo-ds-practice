using CSharp.InterviewCake.Arrays;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class FCFSTest
    {
        [Fact]
        public void BothRegistersHaveSameNumberOfOrdersTest()
        {
            var takeOutOrders = new int[] { 1, 4, 5 };
            var dineInOrders = new int[] { 2, 3, 6 };
            var servedOrders = new int[] { 1, 2, 3, 4, 5, 6 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.True(result);
        }

        [Fact]
        public void RegistersHaveDifferentLengthsTest()
        {
            var takeOutOrders = new int[] { 1, 5 };
            var dineInOrders = new int[] { 2, 3, 6 };
            var servedOrders = new int[] { 1, 2, 6, 3, 5 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.False(result);
        }

        [Fact]
        public void OneRegisterIsEmptyTest()
        {
            var takeOutOrders = new int[] { };
            var dineInOrders = new int[] { 2, 3, 6 };
            var servedOrders = new int[] { 2, 3, 6 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.True(result);
        }

        [Fact]
        public void ServedOrdersIsMissingOrdersTest()
        {
            var takeOutOrders = new int[] { 1, 5 };
            var dineInOrders = new int[] { 2, 3, 6 };
            var servedOrders = new int[] { 1, 6, 3, 5 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.False(result);
        }

        [Fact]
        public void ServedOrdersHasExtraOrders()
        {
            var takeOutOrders = new int[] { 1, 5 };
            var dineInOrders = new int[] { 2, 3, 6 };
            var servedOrders = new int[] { 1, 2, 3, 5, 6, 8 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.False(result);
        }

        [Fact]
        public void OneRegisterHasExtraOrders()
        {
            var takeOutOrders = new int[] { 1, 9 };
            var dineInOrders = new int[] { 7, 8 };
            var servedOrders = new int[] { 1, 7, 8 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.False(result);
        }

        [Fact]
        public void OneRegisterHasUnservedOrders()
        {
            var takeOutOrders = new int[] { 55, 9 };
            var dineInOrders = new int[] { 7, 8 };
            var servedOrders = new int[] { 1, 7, 8, 9 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.False(result);
        }

        [Fact]
        public void OrderNumbersAreNotSequential()
        {
            var takeOutOrders = new int[] { 27, 12, 18 };
            var dineInOrders = new int[] { 55, 31, 8 };
            var servedOrders = new int[] { 55, 31, 8, 27, 12, 18 };
            var result = FCFS.IsFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders);
            Assert.True(result);
        }
    }
}
