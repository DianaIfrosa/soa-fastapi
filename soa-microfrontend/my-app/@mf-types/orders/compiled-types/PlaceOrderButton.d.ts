import React from "react";
interface OrderButtonProps {
    onClick: () => void;
    disabled?: boolean;
    children: React.ReactNode;
}
declare const PlaceOrderButton: ({ onClick, disabled, children }: OrderButtonProps) => import("react/jsx-runtime").JSX.Element;
export default PlaceOrderButton;
