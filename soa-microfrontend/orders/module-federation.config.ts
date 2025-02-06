export const mfConfig = {
  name: "orders",
  filename: 'remoteEntry.js', 
  exposes: {
    "./PlaceOrderButton": "./src/PlaceOrderButton.tsx",
    "./Order": "./src/Order.tsx"
  },
  shared: ["react", "react-dom"],
};
