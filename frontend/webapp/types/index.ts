export type PagedResult<T> = {
    results: T[]
    pageCount: number
    totalCount: number
}

export type Auction = {
    reserve: number
    seller: string
    winner?: string
    soldAmount: number
    reservePrice: number
    currentHighBid: number
    createdAt: string
    updatedAt: string
    auctionEnd: string
    status: string
    make: string
    model: string
    year: number
    colour: string
    mileage: number
    imageUrl: string
    id: string
  }