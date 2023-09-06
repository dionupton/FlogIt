"use client";

import { useParamStore } from "@/hooks/useParamsStore";
import React from "react";
import { usePathname, useRouter } from "next/navigation";
import { GiTakeMyMoney } from "react-icons/gi";

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
      className="cursor-pointer flex items-center gap-2 text-3xl font-semibold text-red-500"
    >
      <GiTakeMyMoney size={34} />
      <div>Flog It Auctions</div>
    </div>
  );
}
