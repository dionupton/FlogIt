'use client'

import { useParamStore } from '@/hooks/useParamsStore'
import { usePathname, useRouter } from 'next/navigation'
import React, { useState } from 'react'
import {FaSearch} from 'react-icons/fa'

export default function Search() {
  const router = useRouter();
  const pathname = usePathname();
  const setParams = useParamStore(state => state.setParams);
  const setSearchValue = useParamStore(state => state.setSearchValue);
  const searchValue = useParamStore(state => state.searchValue);

  function onChange(event: any) {
    setSearchValue(event.target.value);
  }

  function search(){
    if(pathname !== '/') router.push('/');
    setParams({searchTerm: searchValue})
  }

  return (
    <div className='flex w-[50%] items-center border-2 rounded py-2 shadow-sm'>
        <input 
        onKeyDown={(e: any) => {
            if(e.key === 'Enter') search();
        }}
        value={searchValue}
        onChange={onChange}
        type="text"
        placeholder='Search for cars by make, model or colour'
        className='
        input-custom
        text-sm
        text-gray-600'
        />
        <button onClick={search}>
            <FaSearch size={34} className='bg-neutral-500 text-white rounded p-2 cursor-pointer mx-2'/>
        </button>
    </div>
  )
}
