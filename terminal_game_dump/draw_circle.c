static void printPattern(int radius, int lineWidth, double xScale)
{
    double hUnitsPerChar = 1 / xScale;
    double hChars = (2 * radius + lineWidth) / hUnitsPerChar;
    double vChars = 2 * radius + lineWidth;
    // dist represents distance to the center 
    double dist;
    double lineWidth_2 = (double)lineWidth / 2;
    double center = radius + lineWidth_2;
    // for vertical movement 
    for (int j = 0; j <= vChars - 1; j++)
    {
        double y = j + 0.5;
        // for horizontal movement 
        for (int i = 0; i <= hChars - 1; i++)
        {
            double x = (i + 0.5) * hUnitsPerChar;
            dist = Math.Sqrt(
                (x - center) * (x - center) +
                (y - center) * (y - center));

            // dist should be in the range  
            // (radius - lineWidth/2) and (radius + lineWidth/2)  
            // to print stars(*) 
            if (dist > radius - lineWidth_2 &&
                            dist < radius + lineWidth_2)
                Console.Write("*");
            else
                Console.Write(" ");
        }

        Console.WriteLine("");
    }
}
static void Main(string[] args)
{
    printPattern(2, 1, 2);
    printPattern(10, 3, 2);
}
