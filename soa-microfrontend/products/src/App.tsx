import React from "react";
import ReactDOM from "react-dom/client";
import ProductsList from "./ProductsList";
import "./index.css";

const App = () => (
    <div className="mt-10 text-3xl mx-auto max-w-6xl">
      {/* <div>Name: products</div>
      <div>Framework: react-18</div> */}
      <ProductsList/>
    </div>
  );

const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(<App />);