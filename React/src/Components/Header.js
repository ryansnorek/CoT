import { Link } from 'react-router-dom';

export default function Header() {
    return (
        <div id="header">
            <h3>Cot ~tails</h3>
            <nav>
                <Link id="header-report" to="/report">Cot report</Link>
                <Link id="header-account" to="/login">Account</Link> 
            </nav>
        </div>
    )
}