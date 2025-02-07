import React, {useState} from "react";
import Greeting from "users/Greeting";
import Order from "orders/Order";

interface Product {
    id: number;
    name: string;
    price: number;
  }

interface OrderPageProps {
  onOrderSuccess: () => void; // Callback function
  basket: Product[];
}

const OrderPage: React.FC<OrderPageProps> = ({ basket, onOrderSuccess }) => {
  const handleOrder = () => {
    onOrderSuccess()
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-2xl mx-auto space-y-6">
      <Greeting userName={JSON.parse(localStorage.getItem("user") ?? "{}")?.email ?? ""} />
      <Order basket = {basket} onOrderSuccess = {handleOrder}/>
    </div>
  </div>
  );
};

export default OrderPage;