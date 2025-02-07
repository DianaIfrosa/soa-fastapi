import React,  { useState, Suspense } from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Route, Routes, Navigate, useNavigate  } from "react-router-dom";

import "./index.css";

import Login from "users/Login";
import Signup from "users/Signup";
import ProductsPage from "./ProductsPage";
import OrderPage from "./OrderPage";

type Product = {
  id: number;
  name: string;
  price: number;
};

const App = () => {
  const [productsSelected, setProductsSelected] = useState<Product[]>([]);
  const navigate = useNavigate();

  const onOrderSuccess = () => {
    navigate("/products");
  }

  const handleLoginSuccess = (userData: { access_token: string; token_type: string, username: string }) => {
    // Redirect to the products page after successful login
    navigate("/products");
    // Optionally, store the user data in local storage
    localStorage.setItem("user", JSON.stringify(userData));
  };

  const handleSignupSuccess = () => {
    alert("Signed up successfully!")
    navigate("/login")
  };

  const handleOrderFromProductsPage = (products: { id: number, name: string, price: number }[]) => {
    setProductsSelected(products)
    navigate("/order");
  };

  return (
          <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route path="/login" element={
                <Login onLoginSuccess={handleLoginSuccess}/>
            }
            />
            <Route path="/signup" element={
                <Signup onSignupSuccess={handleSignupSuccess}/>
            }
            />
            <Route path="/products" element={
              <ProductsPage onOrderPressed={handleOrderFromProductsPage}/>} />
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/order" element={
                <OrderPage basket = {productsSelected} onOrderSuccess={onOrderSuccess}/>
            }
            />
          </Routes>
          
          </Suspense>
    );
};

const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(
  <Router>
    <App />
  </Router>
);