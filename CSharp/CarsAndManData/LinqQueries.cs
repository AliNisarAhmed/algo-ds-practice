using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace CSharp
{
    public static class LinqQueries
    {
        public static void Run() 
        {
            var cars = ProcessCars(@"C:\web-dev\algo-ds-practice\CSharp\CarsAndManData\fuel.csv");

            var mans = ProcessMans(@"C:\web-dev\algo-ds-practice\CSharp\CarsAndManData\manufacturers.csv");

            var q1 = cars.Where(c => c.Year == 2017).GroupBy(c => c.Manufacturer);

            var q2 = cars.Join(
                mans,
                c => c.Manufacturer,
                m => m.Name,
                (c, m) => new
                    {
                        Car = c,
                        Manufacturer = m
                    })
                .OrderBy(g => g.Manufacturer.Name);

            var q3 = mans.GroupJoin(cars, m => m.Name, c => c.Manufacturer, (m, cg) => new
            {
                Cars = cg,
                Manufacturer = m
            });

            // Top 3 fuel efficeint cars by country

            // country data is in mans, cars in cars


            var q4 =
                mans.GroupJoin(
                    cars,
                    m => m.Name,
                    c => c.Manufacturer,
                    (m, cg) => new
                    {
                        Manufacturer = m,
                        Cars = cg
                    }).GroupBy(a => a.Manufacturer.Headquarters);
                   

            foreach(var group in q4)
            {
                Console.WriteLine(group.Key);
                foreach(var car in group.SelectMany(g => g.Cars).OrderByDescending(c => c.Combined).Take(3))
                {
                    Console.WriteLine($"\t{car.Name}");
                }
                
            }
        }

        private static List<Manufacturer> ProcessMans(string path)
        {
            return File.ReadAllLines(path)
                       .Where(l => l.Length > 1)
                       .Select(l =>
                       {
                           var columns = l.Split(',');
                           return new Manufacturer
                           {
                               Name = columns[0],
                               Headquarters = columns[1],
                               Year = int.Parse(columns[2])
                           };
                       }).ToList();
        }

        public static List<Car> ProcessCars(string path)
        {
            var query =
                File.ReadAllLines(path)
                    .Skip(1)
                    .Where(l => l.Length > 1)
                    .ToCar();

            return query.ToList();
        }
    }

    public class Car
    {
        public int Year { get; set; }
        public string Manufacturer { get; set; }
        public string Name { get; set; }
        public double Displacement { get; set; }
        public int Cylinders { get; set; }
        public int City { get; set; }
        public int Highway { get; set; }
        public int Combined { get; set; }
    }

    public class Manufacturer
    {
        public string Name { get; set; }
        public string Headquarters { get; set; }
        public int Year { get; set; }
    }

    public static class CarExtensions
    {
        public static IEnumerable<Car> ToCar (this IEnumerable<string> source)
        {
            foreach (var line in source)
            {
                var columns = line.Split(',');
                yield return new Car
                {
                    Year = int.Parse(columns[0]),
                    Manufacturer = columns[1],
                    Name = columns[2],
                    Displacement = double.Parse(columns[3]),
                    Cylinders = int.Parse(columns[4]),
                    City = int.Parse(columns[5]),
                    Highway = int.Parse(columns[6]),
                    Combined = int.Parse(columns[7])
                };
            }
        }
    }
}
