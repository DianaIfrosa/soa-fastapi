export const mfConfig = {
  name: "products",
  filename: 'remoteEntry.js', 
  exposes: {
    "./ProductsList": "./src/ProductsList.tsx",
    "./MiniBasket": "./src/MiniBasket.tsx"
  },
  shared: ["react", "react-dom"],
};
