import { isMobile } from "react-device-detect";
import Listings from "./auctions/Listings";

export default function Home() {
  <div>
    {isMobile ? (
      <h3>This website is not optimized for mobile devices.</h3>
    ) : (
      <Listings />
    )}
  </div>
}
