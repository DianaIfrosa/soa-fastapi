import React from "react";

interface GreetingProps {
  userName: string; // Prop for the user's name
}

const Greeting: React.FC<GreetingProps> = ({ userName }) => {
  return (
    <div className=" items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600">
      <div className="bg-white p-8 rounded-lg shadow-2xl text-center transform transition-all hover:scale-105">
        <h1 className="text-4xl font-bold text-gray-800 mb-4 animate-bounce">
          Hi, {userName}! 👋
        </h1>
        <p className="text-lg text-gray-600">
          Welcome to our awesome platform. We're glad to have you here!
        </p>
      </div>
    </div>
  );
};

export default Greeting;