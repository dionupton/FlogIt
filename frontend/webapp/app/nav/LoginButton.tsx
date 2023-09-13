'use client'

import { Button } from 'flowbite-react'
import { signIn } from 'next-auth/react'
import {isMobile} from 'react-device-detect';
import React from 'react'

export default function LoginButton() {
  if(isMobile) return (
    <div></div>
  )
  return (
    <Button outline onClick={() => signIn('id-server', {callbackUrl: '/'}, {prompt: 'login'})}>
        Login
    </Button>
  )
}
