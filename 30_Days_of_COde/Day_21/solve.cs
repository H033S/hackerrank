    using System;

    class Printer
    {

        static void PrintArray<T>(params T[] elements)
        {
            for (int i = 0; i < elements.Length; i++)
            {
                Console.WriteLine(elements[i]);
            }
        }

        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int[] intArray = new int[n];
            for (int i = 0; i < n; i++)
            {
                intArray[i] = Convert.ToInt32(Console.ReadLine());
            }
            
            n = Convert.ToInt32(Console.ReadLine());
            string[] stringArray = new string[n];
            for (int i = 0; i < n; i++)
            {
                stringArray[i] = Console.ReadLine();
            }
            
            PrintArray<Int32>(intArray);
            PrintArray<String>(stringArray);
        }
    }