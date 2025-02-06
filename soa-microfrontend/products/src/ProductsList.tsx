import React, { useState, useEffect } from "react";
import MiniBasket from "./MiniBasket";
import axios from "axios";

type Product = {
  id: number;
  name: string;
  price: number;
};

// const products = [
//   Product (id= 1, name ="Product 1", price= 19.99),
//   { id: 2, name: "Product 2", price: 29.99 },
//   { id: 3, name: "Product 3", price: 39.99 },
// ];


const Products = () => {
  const [basket, setBasket] = useState<{ id: number; name: string; price: number }[]>([]);
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const addToBasket = (product: { id: number; name: string; price: number }) => {
    setBasket([...basket, product]);
  };

  useEffect(() => {
    axios
      .get<Product[]>("http://localhost:8080/api/v1/products/")
      .then((response) => {
        setProducts(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching products:", error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;


  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-center text-gray-900 mb-8">Products</h1>
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <ul className="divide-y divide-gray-200">
            {products.map((product) => (
              <li key={product.id} className="p-4 hover:bg-gray-50 transition-colors">
                <div className="flex justify-between items-center">
                  <div>
                    <h3 className="text-lg font-medium text-gray-900">{product.name}</h3>
                    <p className="text-sm text-gray-500">${product.price.toFixed(2)}</p>
                  </div>
                  <button
                    onClick={() => addToBasket(product)}
                    className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Add to Basket
                  </button>
                </div>
              </li>
            ))}
          </ul>
        </div>
        <div className="mt-8">
          <MiniBasket items={basket} />
        </div>
      </div>
    </div>
  );
};

export default Products;