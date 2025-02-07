import React from "react";
interface Product {
    id: number;
    name: string;
    price: number;
}
interface OrderProps {
    basket: Product[];
    onOrderSuccess: () => void;
}
declare const Order: React.FC<OrderProps>;
export default Order;
