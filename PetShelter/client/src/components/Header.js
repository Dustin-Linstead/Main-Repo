import React from 'react'
import { Link } from '@reach/router';

const Header = () => {
    return (
        <header className="row">
            <h1 className="col-sm-12">Pet Shelter</h1>
            <div>
                <Link to="/pets">Dashboard</Link>&nbsp;
                <Link to="/pets/new">New Pet</Link>
            </div>
        </header>
    )
}

export default Header