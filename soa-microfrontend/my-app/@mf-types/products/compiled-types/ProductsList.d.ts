type ProductsListProps = {
    basket: {
        id: number;
        name: string;
        price: number;
    }[];
    addToBasket: (product: {
        id: number;
        name: string;
        price: number;
    }) => void;
};
declare const ProductsList: ({ basket, addToBasket }: ProductsListProps) => import("react/jsx-runtime").JSX.Element;
export default ProductsList;
