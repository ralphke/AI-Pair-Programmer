using Copilot_C_;
internal class Program
{
    // Main method is the entry point of the application
    private static void Main(string[] args)
    {
        var result = ProcessArguments(args);
        Console.WriteLine(result);
        Console.WriteLine("Enter Date in the Forma YYYY-MM-dd here:");
        var date = Console.ReadLine();
        if (string.IsNullOrEmpty(date) || date.Length != 10 || date.Contains('-') == false)
        {
            Console.WriteLine("Invalid Date input");
            return;
        }
        // Use try construct to avoid errors when casting types from input string
        try
        {
            var dateArray = date.Split('-');
            int year = int.Parse(dateArray[0]);
            int month = int.Parse(dateArray[1]);
            int day = int.Parse(dateArray[2]);
            int days = Copilot_C_.DateCalculations.DaysInMonth(month, year, day);
            // add a composit string format here
            Console.WriteLine($"Days in Month: {days}");
        }
        catch (FormatException)
        {
            Console.WriteLine("Input is a valid date format");
        }

    }

    // This method can be tested independently
    public static string ProcessArguments(string[] args)
    {
        // Check if any arguments were passed
        if (args.Length == 0)
        {
            // If no arguments were passed, return a message
            return "No arguments were passed";
        }
        else
        {
            // If arguments were passed, return them
            return "Arguments passed were: " + string.Join(", ", args);
        }
    }
}