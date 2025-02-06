import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";

import ProductsList from "products/ProductsList";
import PlaceOrderButton from "orders/PlaceOrderButton";

const App = () => (
    <div className="text-3xl mx-auto max-w-6xl">
        <ProductsList />
        <div className="text-center">
            <img
                src="https://mdbcdn.b-cdn.net/img/new/avatars/8.webp"
                className="rounded-full w-32 mb-4 mx-auto"
                alt="Avatar"
            />
            <h5 className="text-xl font-medium leading-tight mb-2">John Doe</h5>
            <p className="text-gray-500">Web designer</p>
        </div>
        <PlaceOrderButton />
    </div>
);


const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(<App />);