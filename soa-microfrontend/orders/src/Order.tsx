import React, { useState } from "react";
import OrderButton from "./PlaceOrderButton";

interface Product {
  id: number;
  name: string;
  price: number;
}

interface OrderProps {
  basket: Product[];
  onOrderSuccess: () => void; // Callback function
}

const Order: React.FC<OrderProps> = ({ basket, onOrderSuccess }) => {
  const [address, setAddress] = useState("");

  // Calculate the total price from the basket
  const totalPrice = basket?.reduce((sum, product) => sum + product.price, 0);

  const handlePlaceOrder = async () => {
    if (!address.trim()) {
      alert("Please enter a valid address.");
      return;
    }
    const datenow = new Date().toISOString()
    try {
      const requestBody = {
        user_id: 1,
        product_ids: basket.map(item => item.id),
        date: datenow,
        address: address
      };

      const response = await fetch("http://localhost:8080/api/v1/orders/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Order placed with products:", basket);
        console.log("Delivery address:", address);
        alert("Order placed successfully!");
        setAddress(""); // Clear the address field
        onOrderSuccess(); // Trigger the success callback
      } else {
        const errorData = await response.json();
        alert("Something went wrong!")
        console.error("Order failed:", errorData);
      }
    } catch (error) {
      alert("Something went wrong");
      console.error("Error during order:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mt-8 bg-white shadow sm:rounded-lg p-6">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Your Order</h2>
          <ul className="divide-y divide-gray-200">
            {basket?.map((product) => (
              <li key={product.id} className="py-2">
                <div className="flex justify-between items-center">
                  <p className="text-sm text-gray-900">{product.name}</p>
                  <p className="text-sm text-gray-500">${product.price?.toFixed(2)}</p>
                </div>
              </li>
            ))}
          </ul>
          <div className="mt-4 pt-4 border-t border-gray-200">
            <div className="flex justify-between items-center">
              <p className="text-lg font-medium text-gray-900">Total</p>
              <p className="text-lg font-bold text-indigo-600">${totalPrice?.toFixed(2)}</p>
            </div>
          </div>
          <div className="mt-6">
            <label htmlFor="address" className="block text-sm font-medium text-gray-700">
              Delivery Address
            </label>
            <input
              id="address"
              name="address"
              type="text"
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Enter your address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>
          <div className="mt-6">
            <OrderButton onClick={handlePlaceOrder}>Place Order</OrderButton>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Order;