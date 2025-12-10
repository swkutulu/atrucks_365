import { useNavigate } from 'react-router-dom';
import { URLS } from '@/constants';
import { Button } from 'primereact/button';

const NotFound = () => {
    const navigate = useNavigate();
    const goHome = () => {
        navigate(URLS.HOME);
    };
    return (
        <div className="flex w-screen items-center justify-center">
            <div className="flex flex-col items-center gap-10 p-10">
                <h1>404</h1>
                <h3>Страница не найдена</h3>
                <Button onClick={goHome}>На главную</Button>
            </div>
        </div>
    );
};

export default NotFound