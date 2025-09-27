import { Link, useLocation } from "react-router-dom"
import { home, managment } from '../../settings/settings.js'

const Navigation = () => {
    const location = useLocation()
    return (
        <ul className="">
            <li className={location.pathname === home ? "active" : null}>
                <Link to={home}>Home</Link>
            </li>
            <li className={location.pathname === managment  ? "active" : null}>
                <Link to={managment}>Management</Link>
            </li>
        </ul>
    )
}

export default Navigation