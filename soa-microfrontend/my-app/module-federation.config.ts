export const mfConfig = {
  name: "my_app",
  filename: 'remoteEntry.js', 
  exposes: {},
  remotes: {
      users: "users@http://localhost:3001/remoteEntry.js",
      products: "products@http://localhost:3002/remoteEntry.js",
      orders: "orders@http://localhost:3003/remoteEntry.js"
  },
  shared: ["react", "react-dom"],
};
