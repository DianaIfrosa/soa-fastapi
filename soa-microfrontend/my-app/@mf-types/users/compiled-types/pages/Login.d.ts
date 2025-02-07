import React from "react";
interface LoginProps {
    onLoginSuccess: (userData: {
        access_token: string;
        token_type: string;
        username: string;
    }) => void;
}
declare const Login: React.FC<LoginProps>;
export default Login;
