using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp.InterviewCake.Arrays
{
    public static class FCFS
    {
        public static bool IsFirstComeFirstServed (
            int[] takeout,
            int[] dinein,
            int[] served)
        {
            var i = 0;
            var j = 0;

            if (takeout.Length + dinein.Length != served.Length)
                return false;

            foreach(var s in served)
            {
                if (i < takeout.Length && j < dinein.Length && s != takeout[i] && s != dinein[j])
                {
                    return false;
                }

                if (i < takeout.Length && takeout[i] == s)
                {
                    i++;
                }
                else if (j < dinein.Length && dinein[j] == s)
                {
                    j++;
                }
            }

            return true;
        }
    }
}
