using Contracts;
using MassTransit;
using Microsoft.AspNetCore.SignalR;

namespace NotificationService.Consumers
{
    public class AuctionFinishedConsumer : IConsumer<AuctionFinished>
    {
        private readonly IHubContext<NotificationHub> hubContext;


        public AuctionFinishedConsumer(IHubContext<NotificationHub> hubContext)
        {
            this.hubContext = hubContext;
        }

        public async Task Consume(ConsumeContext<AuctionFinished> context)
        {
            Console.WriteLine("---> auction finished message received");

            await hubContext.Clients.All.SendAsync("AuctionFinished", context.Message);
        }

    }
}