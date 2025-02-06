import React from "react";

interface MiniBasketProps {
  items: { id: number; name: string; price: number }[];
}

const MiniBasket = ({ items }: MiniBasketProps) => (
  <div className="bg-white shadow sm:rounded-lg p-6">
    <h2 className="text-lg font-medium text-gray-900 mb-4">Mini Basket</h2>
    {items.length === 0 ? (
      <p className="text-sm text-gray-500">Your basket is empty.</p>
    ) : (
      <ul className="divide-y divide-gray-200">
        {items.map((item) => (
          <li key={item.id} className="py-2">
            <div className="flex justify-between items-center">
              <p className="text-sm text-gray-900">{item.name}</p>
              <p className="text-sm text-gray-500">${item.price.toFixed(2)}</p>
            </div>
          </li>
        ))}
      </ul>
    )}
  </div>
);

export default MiniBasket;