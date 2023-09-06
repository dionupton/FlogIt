'use client'

import { useParamStore } from '@/hooks/useParamsStore'
import React from 'react'
import { GiTakeMyMoney } from 'react-icons/gi'

export default function Logo() {
const reset = useParamStore(state => state.reset);


  return (
    <div onClick={reset} className='cursor-pointer flex items-center gap-2 text-3xl font-semibold text-red-500'>
    <GiTakeMyMoney size={34}/>
    <div>Flog It Auctions</div>
  </div>
  )
}
