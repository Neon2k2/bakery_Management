using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
internal class Program
{
    private static void Main(string[] args)
    {
        Dictionary<int, string> map = new Dictionary<int, string>{
            { 1, "Add_order" },
            { 2, "View_order" },
            { 3, "Update_order" },
            { 4, "export"}
        };

        Dictionary<string, Action<OrderContext>> action = new Dictionary<string, Action<OrderContext>>{
            { "Add_order", (db) => AddOrder(db)},
            { "View_order", (db) => ViewOrder(db)},
            { "Update_order", (db) => UpdateOrder(db)},
            { "export", (db) => Export(db)}
        };

        using var db = new OrderContext();

        Console.WriteLine($"{db.DbPath}.");


        while (true)
        {
            Console.WriteLine("Hi Welcome to the Bakery Application");
            Console.WriteLine("Choose the option");
            foreach (var kvp in map)
            {
                Console.WriteLine($"{kvp.Key}: {kvp.Value}");
            }
            Console.WriteLine("5: Exit");
            Console.WriteLine();

            int choice = int.Parse(Console.ReadLine());

            if (choice == 5)
            {
                break;
            }
            if (map.ContainsKey(choice))
            {
                action[map[choice]].Invoke(db);
            }
            else
            {
                Console.WriteLine("Invalid choice. Please choose again.");
            }
        }
    }

    static void AddOrder(OrderContext db)
    {
        Console.Write("Enter the name of the customer: ");
        string name = GetValidInput("^[A-Za-z]+$", "Please enter only letters for the name: ");

        Console.Write("Enter the item being purchased: ");
        string item = GetValidInput("^[A-Za-z]+$", "Please enter only letters for the item: ");

        Console.Write("Enter the quantity: ");
        int.TryParse(Console.ReadLine(), out int quantity);

        db.Add(new Order { Customer = name, Quantity = quantity, Item = item });
        db.SaveChanges();
        Console.WriteLine("Successfully added...");
    }

    static string GetValidInput(string pattern, string errorMessage)
    {
        string input;
        do
        {
            input = Console.ReadLine();
            if (!Regex.IsMatch(input, pattern))
            {
                Console.Write(errorMessage);
            }
        } while (!Regex.IsMatch(input, pattern));

        return input;
    }

    static void ViewOrder(OrderContext db)
    {
        var orders = db.Orders.ToList();

        if (orders.Count > 0)
        {
            Console.WriteLine("-".PadRight(55, '-'));
            Console.WriteLine("Order Id | Customer | Item | Quantity");
            Console.WriteLine("-".PadRight(55, '-'));
            foreach (var order in orders)
            {
                Console.WriteLine($"{order.Id} | {order.Customer} | {order.Item} | {order.Quantity}");
            }
        }
        else
        {
            Console.WriteLine("No records to View...");
        }
    }

    static void UpdateOrder(OrderContext db)
    {
        Console.Write("Enter the customer name to update the order: ");
        string customer = Console.ReadLine();

        var order = db.Orders.FirstOrDefault(o => o.Customer == customer);

        if (order != null)
        {
            Console.Write("Enter the new item: ");
            string newItem = Console.ReadLine();
            Console.Write("Enter the new quantity: ");
            int.TryParse(Console.ReadLine(), out int newQuantity);

            order.Quantity = newQuantity;
            order.Item = newItem;
            db.SaveChanges();
            Console.WriteLine("Order updated successfully.");
        }
        else
        {
            Console.WriteLine("Order not found.");
        }
    }

    static void Export(OrderContext db)
    {
        var orders = db.Orders.ToList();

        if (orders.Count > 0)
        {
            string csvFilePath = "orders.csv";

            using (StreamWriter writer = new StreamWriter(csvFilePath))
            {
                writer.WriteLine("Order Id, Customer, Item, Quantity");

                foreach (var order in orders)
                {
                    writer.WriteLine($"{order.Id},{order.Customer},{order.Item},{order.Quantity}");
                }
            }

            Console.WriteLine($"Orders exported to {csvFilePath} successfully.");
        }
        else
        {
            Console.WriteLine("No orders to export.");
        }
    }
}
