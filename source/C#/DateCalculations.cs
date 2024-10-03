using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Copilot_C_
{
    public class DateCalculations

    { 
        public static int DaysInMonth(int month, int year, int day)
        {
            if (month < 1 || month > 12 || day < 1)
                return 0;

            if (month == 2)
                return year % 4 == 0 ? 29 : 28;

            if (month == 4 || month == 6 || month == 9 || month == 11)
                return day > 30 ? 0 : 30;

            return day > 31 ? 0 : 31;
        }

        public static int DaysInYear(int year, int month, int day)
        {
            if (month < 1 || month > 12 || day < 1)
                return 0;

            if (month == 2)
                return year % 4 == 0 ? 366 : 365;

            if (month == 4 || month == 6 || month == 9 || month == 11)
                return day > 30 ? 365 : 366;

            return day > 31 ? 365 : 366;
        }

    }
}