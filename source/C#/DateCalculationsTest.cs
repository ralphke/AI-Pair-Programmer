using NUnit.Framework;
using Copilot_C_;

[TestFixture]
public class DateCalculationsTests
{
    [Test]
    public void DaysInMonth_ValidMonth_ReturnsCorrectNumberOfDays()
    {
        // Arrange
        int month = 1;
        int year = 2022;
        int day = 1;
        int expected = 31;

        // Act
        int actual = DateCalculations.DaysInMonth(month, year, day);

        // Assert
        Assert.Equals(expected, actual);
    }

    [Test]
    public void DaysInMonth_InvalidMonth_ReturnsZero()
    {
        // Arrange
        int month = 13;
        int year = 2022;
        int day = 1;
        int expected = 0;

        // Act
        int actual = DateCalculations.DaysInMonth(month, year, day);

        // Assert
        Assert.Equals(expected, actual);
    }

    [Test]
    public void DaysInYear_ValidYear_ReturnsCorrectNumberOfDays()
    {
        // Arrange
        int year = 2022;
        int month = 1;
        int day = 1;
        int expected = 365;

        // Act
        int actual = DateCalculations.DaysInYear(year, month, day);

        // Assert
        Assert.Equals(expected, actual);
    }

    [Test]
    public void DaysInYear_InvalidYear_ReturnsZero()
    {
        // Arrange
        int year = 0;
        int month = 1;
        int day = 1;
        int expected = 0;

        // Act
        int actual = DateCalculations.DaysInYear(year, month, day);

        // Assert
        Assert.Equals(expected, actual);
    }
}