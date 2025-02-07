export const mfConfig = {
  name: "users",
  filename: 'remoteEntry.js', 
  exposes: {
    "./Login": "./src/pages/Login.tsx",
    "./Signup": "./src/pages/Signup.tsx",
    "./Greeting": "./src/pages/Greeting.tsx"
  },
  shared: ["react", "react-dom"],
};
