import React from "react";
import ReactDOM from "react-dom/client";
import Order from "./Order";
import "./index.css";

const App = () => (
    <div className="mt-10 text-3xl mx-auto max-w-6xl">
    {/* <Order basket = {[]} onOrderSuccess={}/> */}
    Hello!
    </div>
  );

const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(<App />);