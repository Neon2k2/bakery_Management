using Microsoft.EntityFrameworkCore;
public class OrderContext : DbContext
{
    public DbSet<Order> Orders { get; set; }
    public string DbPath { get; }

    public OrderContext()
    {
        // var folder = Environment.SpecialFolder.Documents;
        var path = @"C:\Users\neon\Desktop\bakery_Management\version_using_aspnetcore\Bakery_App\Data";
        DbPath = System.IO.Path.Join(path, "Orders.db");
    }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlite($"Data Source={DbPath}");
    }
}
