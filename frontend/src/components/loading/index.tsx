export const Loading = () => {
    return (
        <div className="card mx-auto self-center flex-1">
            <i className="pi pi-spin pi-cog text-7xl! text-stone-500"></i>
        </div>
    );
};

export const LoadingFull = () => {
    return (
        <div className="mx-auto flex align-center justify-center h-screen w-100 flex-1">
            <i className="pi pi-spin pi-cog text-7xl! text-stone-500 justify-self-center self-center"></i>
        </div>
    );
};
