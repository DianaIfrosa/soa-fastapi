import React from "react";
import ReactDOM from "react-dom/client";
import ProductsList from "./ProductsList";
import "./index.css";

interface Product {
  id: number;
  name: string;
  price: number;
}

const products: Product[] = [
  { id: 1, name: 'Laptop', price: 1299 },
  { id: 2, name: 'Smartphone', price: 799 },
  { id: 3, name: 'Headphones', price: 199 },
  { id: 4, name: 'Monitor', price: 299 },
]; 

const App = () => (
    <div className="mt-10 text-3xl mx-auto max-w-6xl">
      {/* <div>Name: products</div>
      <div>Framework: react-18</div> */}
      <ProductsList basket = {products} addToBasket={() => {
      console.log('Add successful!');
    } }/>
    </div>
  );

const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(<App />);