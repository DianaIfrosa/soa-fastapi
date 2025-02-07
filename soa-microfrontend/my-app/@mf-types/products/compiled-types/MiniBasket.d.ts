interface MiniBasketProps {
    items: {
        id: number;
        name: string;
        price: number;
    }[];
}
declare const MiniBasket: ({ items }: MiniBasketProps) => import("react/jsx-runtime").JSX.Element;
export default MiniBasket;
