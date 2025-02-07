
    export type RemoteKeys = 'products/ProductsList' | 'products/MiniBasket';
    type PackageType<T> = T extends 'products/MiniBasket' ? typeof import('products/MiniBasket') :T extends 'products/ProductsList' ? typeof import('products/ProductsList') :any;