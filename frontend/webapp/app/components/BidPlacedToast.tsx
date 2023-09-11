import { Auction, Bid } from '@/types'
import Link from 'next/link'
import React from 'react'
import Image from 'next/image'

type Props = {
    bid: Bid
    auction: Auction
}

export default function AuctionCreatedToast({bid, auction} : Props) {
  return (
    <Link href={`/auctions/details/${bid.auctionId}`} className='flex flex-col items-center'>
        <div className='flex flex-row items-center gap-2'>
            <Image 
                src={auction.imageUrl}
                alt='image'
                height={80}
                width={80}
                className='rounded-lg w-auto h-auto'          
            />

            <span>£{bid.amount} bid placed on {auction.make} {auction.model} </span>
        </div>
        </Link>
  )
}
