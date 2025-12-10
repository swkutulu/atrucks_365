import { NavLink } from 'react-router';
import { URLS } from '@/constants';
import { useAppSelector } from '@/store';


const Home = () => {
    const { isAuthenticated, token } = useAppSelector((store) => store.auth);

    return (
        <div className="flex flex-col items-top justify-center flex-1">
            <div className="flex flex-col items-center gap-10 p-10">
                <NavLink to={URLS.HOME} className="text-3xl">
                    Home<i className="ml-5 pi pi-arrow-right"></i>
                </NavLink>
            </div>
        </div>
    );
};

export default Home;

