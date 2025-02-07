
    export type RemoteKeys = 'users/Login' | 'users/Signup' | 'users/Greeting';
    type PackageType<T> = T extends 'users/Greeting' ? typeof import('users/Greeting') :T extends 'users/Signup' ? typeof import('users/Signup') :T extends 'users/Login' ? typeof import('users/Login') :any;