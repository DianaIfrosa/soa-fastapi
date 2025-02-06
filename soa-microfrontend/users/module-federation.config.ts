export const mfConfig = {
  name: "users",
  filename: 'remoteEntry.js', 
  exposes: {
    "./Login": "./src/pages/Login.tsx",
    "./Signup": "./src/pages/Signup.tsx"
  },
  shared: ["react", "react-dom"],
};
