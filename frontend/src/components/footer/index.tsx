import { Link } from 'react-router';
import moment from 'moment';
import { URLS } from '@/constants';
import Logo from '@/assets/images/logo.svg';

export const AppFooter = () => {
    const year = moment().format('YYYY');
    return (
        <footer className="flex grow-0 shrink-0 items-center justify-between py-1 px-5 border-t border-primary-200 bg-header text-header-text">
            <Link to={URLS.HOME}>
                <img src={Logo} className="h-[0.8rem]" />
            </Link>
            <div className="text-xs">
            </div>
            <div className="gap-2 text-xs">
                Все права защищены © {year}
            </div>
        </footer>
    );
};
