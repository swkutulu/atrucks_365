interface Res {
    data: unknown;
    message: string;
}

interface ApiError {
    status: number;
    data: object;
}