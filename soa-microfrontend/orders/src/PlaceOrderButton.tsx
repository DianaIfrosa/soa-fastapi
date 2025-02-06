import React from "react"

interface OrderButtonProps {
    onClick: () => void;
    disabled?: boolean;
    children: React.ReactNode;
  }
  
  const PlaceOrderButton = ({ onClick, disabled = false, children }: OrderButtonProps) => {
    return (
      <button
        onClick={onClick}
        disabled={disabled}
        className={`w-full inline-flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white ${
          disabled
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        }`}
      >
        {children}
      </button>
    );
  };

export default PlaceOrderButton;
  