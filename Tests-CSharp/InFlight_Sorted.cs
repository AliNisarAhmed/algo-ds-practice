using CSharp.InterviewCake.HashTables;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class InFlight_Sorted
    {
        [Fact]
        public void Get_Times_From_Sorted()
        {
            var result = HashTableClass.InFlight_Sorted(
                new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
                12
                );

            Assert.True(result);
        }
    }
}
