"use client";

import { useParamStore } from "@/hooks/useParamsStore";
import React from "react";
import { usePathname, useRouter } from "next/navigation";

export default function Logo() {
  const router = useRouter()
  const pathname = usePathname();
  const reset = useParamStore((state) => state.reset);

  function doReset() {
    if(pathname !== '/') router.push('/');
    reset();
  }

  return (
    <div
      onClick={doReset}
      className="cursor-pointer flex items-center gap-2 text-3xl font-bold"
    >
      
      <div>FLOG IT</div>
    </div>
  );
}
