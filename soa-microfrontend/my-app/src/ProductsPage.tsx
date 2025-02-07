import React, { useState } from "react";
import Greeting from "users/Greeting";
import ProductsList from "products/ProductsList";
import OrderButton from "orders/PlaceOrderButton";

interface ProductsPageProps {
  onOrderPressed: (products: {id: number; name: string; price: number }[]) => void; // Callback function
}

type Product = {
  id: number;
  name: string;
  price: number;
};

const ProductsPage: React.FC<ProductsPageProps> = ({ onOrderPressed }) => {
  const [basket, setBasket] = useState<Product[]>([]);

  const addToBasket = (product: Product) => {
    setBasket([...basket, product]);
  };

  const handleOrder = () => {
    onOrderPressed(basket)
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-2xl mx-auto space-y-6">
      <Greeting userName={JSON.parse(localStorage.getItem("user") ?? "{}")?.email ?? ""} />
      <ProductsList basket={basket} addToBasket ={addToBasket}/>
      <OrderButton onClick={handleOrder}>Order</OrderButton>
    </div>
  </div>
  );
};

export default ProductsPage;