import React, { useState } from "react";
import OrderButton from "./PlaceOrderButton";

// Sample selected products data (passed from the previous page)
const selectedProducts = [
  { id: 1, name: "Product 1", price: 19.99 },
  { id: 2, name: "Product 2", price: 29.99 },
  { id: 3, name: "Product 3", price: 39.99 },
];

const Order = () => {
  const [address, setAddress] = useState("");

  const totalPrice = selectedProducts.reduce((sum, product) => sum + product.price, 0);

  const handlePlaceOrder = () => {
    if (!address.trim()) {
      alert("Please enter a valid address.");
      return;
    }

    // Call backend /orders endpoint to place the order
    console.log("Order placed with products:", selectedProducts);
    console.log("Delivery address:", address);
    alert("Order placed successfully!");
    setAddress(""); // Clear the address field
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-center text-gray-900 mb-8">Orders</h1>
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <ul className="divide-y divide-gray-200">
            {selectedProducts.map((product) => (
              <li key={product.id} className="p-4">
                <div className="flex justify-between items-center">
                  <div>
                    <h3 className="text-lg font-medium text-gray-900">{product.name}</h3>
                    <p className="text-sm text-gray-500">${product.price.toFixed(2)}</p>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
        <div className="mt-8 bg-white shadow sm:rounded-lg p-6">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Your Order</h2>
          <ul className="divide-y divide-gray-200">
            {selectedProducts.map((product) => (
              <li key={product.id} className="py-2">
                <div className="flex justify-between items-center">
                  <p className="text-sm text-gray-900">{product.name}</p>
                  <p className="text-sm text-gray-500">${product.price.toFixed(2)}</p>
                </div>
              </li>
            ))}
          </ul>
          <div className="mt-4 pt-4 border-t border-gray-200">
            <div className="flex justify-between items-center">
              <p className="text-lg font-medium text-gray-900">Total</p>
              <p className="text-lg font-bold text-indigo-600">${totalPrice.toFixed(2)}</p>
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