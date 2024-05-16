using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;


public class Order
{
    public int Id { get; set; }
    public string Customer { get; set; }
    public string Item { get; set; }
    public int Quantity { get; set; }
}