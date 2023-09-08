using Contracts;
using MassTransit;
using Microsoft.AspNetCore.SignalR;

namespace NotificationService.Consumers
{
    public class BidPlacedConsumer : IConsumer<BidPlaced>
    {
        private readonly IHubContext<NotificationHub> hubContext;


        public BidPlacedConsumer(IHubContext<NotificationHub> hubContext)
        {
            this.hubContext = hubContext;
        }

        public async Task Consume(ConsumeContext<BidPlaced> context)
        {
            Console.WriteLine("---> bid placed message received");

            await hubContext.Clients.All.SendAsync("BidPlaced", context.Message);
        }
    }
}