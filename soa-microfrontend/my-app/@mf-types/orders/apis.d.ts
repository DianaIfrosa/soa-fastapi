
    export type RemoteKeys = 'orders/PlaceOrderButton' | 'orders/Order';
    type PackageType<T> = T extends 'orders/Order' ? typeof import('orders/Order') :T extends 'orders/PlaceOrderButton' ? typeof import('orders/PlaceOrderButton') :any;